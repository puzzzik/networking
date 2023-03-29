from rest_framework.decorators import api_view
from rest_framework.request import Request


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


@api_view(['POST'])
def get_file(request: Request):
    request_user = request.user
    user = User.objects.get(pk=request_user.pk)