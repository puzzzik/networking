# Generated by Django 4.2 on 2023-05-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_file_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='last_modified',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]