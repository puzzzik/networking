# Generated by Django 4.2 on 2023-05-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_file_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
