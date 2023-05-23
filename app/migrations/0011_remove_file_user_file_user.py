# Generated by Django 4.2 on 2023-05-23 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_file_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='file', to=settings.AUTH_USER_MODEL),
        ),
    ]
