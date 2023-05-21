from django.contrib.auth import authenticate
from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import *


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', "name", "last_modified", "size", "hash"]
        read_only_fields = ['id', "last_modified", "size", "hash"]


# class FolderSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     files = FileSerializer(many=True)
#
#     class Meta:
#         # model = Folder
#
#         fields = ["files"]
