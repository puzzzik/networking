from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes
from rest_framework.response import Response
from django.core.files.uploadedfile import InMemoryUploadedFile
from .serializers import *
from authentication.models import User


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
    file = File.objects.get(pk=request.file_id)
    file_serializer = FileSerializer(file)
    return Response(file_serializer.data)


@extend_schema(request=FileSerializer)
@api_view(['POST'])
def post_file_info(request: Request):
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)
    files = request.FILES
    print(files)
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
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)
    file: InMemoryUploadedFile = request.FILES['file_field']
    print(file.name)
    print(file.size)
    print(file.content_type)
    return Response()