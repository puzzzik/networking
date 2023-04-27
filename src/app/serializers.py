from django.contrib.auth import authenticate
from rest_framework import serializers
from backend.authentication.serializers import UserSerializer
from .models import *


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', "name", "last_modified", "size", "hash", "url"]


class FolderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    files = FileSerializer(many=True)

    class Meta:
        model = Folder

        fields = ['id', "user", "files", "name"]
