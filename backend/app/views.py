from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes
from rest_framework.response import Response
from django.core.files.uploadedfile import InMemoryUploadedFile
from .serializers import *
from authentication.models import User
from ..grpc_client.client import Client
@extend_schema(responses=FileSerializer(many=True))
@api_view(['GET'])
def list_files(request: Request):
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)
    try:
        folder = Folder.objects.get(user__pk=user.pk)
        folder_serializer = FolderSerializer(folder)
        return Response(folder_serializer.data)

    except:
        return Response([], status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    responses=FileSerializer,
    parameters=[
        OpenApiParameter("file_id", OpenApiTypes.INT)
    ]
)
@api_view(['GET'])
def get_file(request: Request):
    try:
        file = File.objects.get(pk=request.file_id)
        info = grpc_client.Client.get_file_info(bucket_name=file.folder.name, file_name=file.name)
        file_serializer = FileSerializer(name=info.name, last_modified=info.date, hash=info.hash)
        return Response(file_serializer.data)
    except:
        return Response()


@extend_schema(request=FileSerializer)
@api_view(['POST'])
def post_file_info(request: Request):
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)
    return Response()


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "file_field": {"type": "string", "format": "binary"}
            },
        },
    },
)
@api_view(['POST'])
def post_file(request: Request):
    file: InMemoryUploadedFile = request.FILES['file_field']
    print(file.name)
    print(file.size)
    print(file.content_type)
    Client.upload_file(bucket_name="test", chunk_data=file.chunks())
    return Response()
