# Generated by Django 4.2 on 2023-05-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_file_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='last_modified',
            field=models.CharField(max_length=100),
        ),
    ]