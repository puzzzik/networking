# Generated by Django 4.2 on 2023-05-20 17:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_folder_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
