from django.db import models
from authentication.models import User
from django.utils.timezone import now as date_now


class File(models.Model):
    name = models.CharField(max_length=100)
    last_modified = models.CharField(max_length=100)
    size = models.FloatField(default=0)
    hash = models.CharField(max_length=300)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_bucket_name(self):
        return self.user.get().get_bucket_name()


# class Folder(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='folder',
#                                 related_query_name='folder')
#     name = models.CharField(max_length=100)
#     files = models.ManyToManyField(File)
#
#     def __str__(self):
#         return self.user.get_short_name() + 'folder'
