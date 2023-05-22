from datetime import datetime
import hashlib

import grpc
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.files.uploadedfile import InMemoryUploadedFile

import unidecode
from .serializers import *
from authentication.models import User
from grpc_client.client import Client
from drf_yasg.utils import swagger_auto_schema, no_body
from drf_yasg.openapi import Parameter, Schema
from backend import redis_connect
from drf_yasg import openapi
from grpc_client.file_service_pb2 import MetaData
from django.http import HttpResponse, JsonResponse
from django.core import exceptions
from wsgiref.util import FileWrapper
import unicodedata
from io import BytesIO
from rest_framework.generics import get_object_or_404


@swagger_auto_schema(methods=['get'], responses={200: FileSerializer(many=True)})
@api_view(['GET'])
def list_files(request: Request):
    user = User.objects.get(pk=request.user.pk)
    file_list: list[MetaData] = Client().get_file_list(user.get_bucket_name())
    files_in_db = user.file_set.all()
    for metadata in file_list:
        file, created = files_in_db.get_or_create(
            name=metadata.filename,
            defaults={
                'name': metadata.filename,
                'last_modified': metadata.last_modified,
                'hash': metadata.hash,
                'size': metadata.size
            }
        )
        if not created:
            file.last_modified = metadata.last_modified
            file.hash = metadata.hash
            file.size = file.size
        else:
            user.file_set.add(file)
        file.save()
    files_in_db.exclude(name__in=[f.filename for f in file_list]).delete()
    try:
        files_serializer = FileSerializer(user.file_set.all(), many=True)
        return Response(files_serializer.data)
    except Exception as e:
        print(e)
    return Response(status=status.HTTP_404_NOT_FOUND)


file_parameter = Parameter('file_name', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)


@swagger_auto_schema(
    methods=['get'],
    responses={
        200: openapi.Schema(type=openapi.TYPE_FILE, format=openapi.FORMAT_BINARY),
        404: "Not Found",
    },
    manual_parameters=[file_parameter]
)
@api_view(['GET'])
def get_file(request: Request):
    file_name: str = request.query_params.get('file_name')
    user = User.objects.get(pk=request.user.pk)
    # file_serializer = FileSerializer(request.data)
    # file = File.objects.get(name=file_name)
    # user.folder.files.objects.get(name=)
    # info = Client().download_file(bucket_name=)
    # file_serializer = FileSerializer(name=info.name, last_modified=info.date, hash=info.hash)
    try:
        response = Client().download_file(bucket_name=user.get_bucket_name(), file_name=file_name)
    except grpc.RpcError as e:
        print(e)
        return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

    data = response.chunk_data
    meta = response.meta

    db_file, created = user.file_set.get_or_create(name=meta.filename, defaults={
        'name': meta.filename,
        'size': meta.size,
        'hash': meta.hash,
        'last_modified': meta.last_modified
    })
    if not created:
        db_file.size = meta.size
        db_file.hash = meta.hash
        db_file.last_modified = meta.last_modified
    response = HttpResponse(data, content_type='application/octet-stream')
    response['Content-Disposition'] = unidecode.unidecode('attachment; filename="' + file_name + '"')
    return response


@swagger_auto_schema(methods=['post'], request_body=FileSerializer, responses={200: FileSerializer()})
@api_view(['POST'])
def post_file_info(request: Request):
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)
    return Response()


@swagger_auto_schema(
    methods=['post'],
    manual_parameters=[
        Parameter(name='file', in_=openapi.IN_FORM, type=openapi.TYPE_FILE, required=True),
        Parameter(name='last_modified', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, required=True)
    ],
    responses={
        200: FileSerializer(),
        409: "Old file",
        302: "Equal file",
        400: "Error"
    }
)
@api_view(['POST'])
def post_file(request: Request):
    user = User.objects.get(pk=request.user.pk)
    uploaded_file: InMemoryUploadedFile = request.FILES['file']
    file = File(
        name=uploaded_file.name,
        size=uploaded_file.size,
        last_modified=request.data['last_modified'],
        hash=md5(uploaded_file)
    )

    try:
        server_file_meta = Client().get_file_info(bucket_name=user.get_bucket_name(), file_name=uploaded_file.name)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            file.save()
            user.file_set.filter(name=file.name).delete()
            user.file_set.add(file)
            metadata: MetaData = Client().upload_file(file=file, data=uploaded_file)
            file.size = metadata.size
            file.hash = metadata.hash
            file.last_modified = metadata.last_modified
            file.save()

            return Response(FileSerializer(file).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if server_file_meta.hash == file.hash:
        return Response("Equal file", status=status.HTTP_302_FOUND)

    if file.last_modified < server_file_meta.last_modified:
        return Response("Old file", status=status.HTTP_409_CONFLICT)
    else:
        file.save()
        user.file_set.filter(name=file.name).delete()
        user.file_set.add(file)
        metadata: MetaData = Client().upload_file(file=file, data=uploaded_file)
        file.size = metadata.size
        file.hash = metadata.hash
        file.last_modified = metadata.last_modified
        file.save()
    return Response(FileSerializer(file).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request: Request):
    user = User.objects.get(pk=request.user.pk)
    response = Response(status=status.HTTP_200_OK)
    response.delete_cookie(key='uid')
    redis_connect.delete(user.pk)
    return response


@swagger_auto_schema(
    methods=['delete'],
    manual_parameters=[
        Parameter(name='file_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
    ],
    responses={
        200: "OK",
        204: "No Content"
    }
)
@api_view(['DELETE'])
def remove_file(request: Request):
    user = User.objects.get(pk=request.user.pk)
    file_name = request.query_params.get('file_name')
    try:
        Client().remove_file(file_name=file_name, bucket_name=user.get_bucket_name())
    except:
        return Response("No Content", status=status.HTTP_204_NO_CONTENT)
    try:
        user.file_set.get(name=file_name).delete()
    except:
        pass
    return Response("OK", status=status.HTTP_200_OK)


def md5(file: InMemoryUploadedFile):
    hash_md5 = hashlib.md5()
    for chunk in file.chunks():
        hash_md5.update(chunk)
    return hash_md5.hexdigest()
