from django.db import models
from backend.authentication import User
from django.utils.timezone import now as date_now


class File(models.Model):
    name = models.CharField(max_length=100)
    last_modified = models.DateTimeField(default=date_now, blank=True)
    size = models.FloatField(default=0)
    hash = models.CharField(max_length=300)
    url = models.URLField()

    def __str__(self):
        return self.name


class Folder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='folder',
                                related_query_name='folder')
    name = models.CharField(max_length=100)
    files = models.ForeignKey(File, on_delete=models.CASCADE, related_name='folder', blank=True, null=True)

    def __str__(self):
        return self.user.get_short_name() + 'folder'
