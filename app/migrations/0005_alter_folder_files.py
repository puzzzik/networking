# Generated by Django 4.2 on 2023-05-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_folder_files_folder_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='files',
            field=models.ManyToManyField(related_name='folder', to='app.file'),
        ),
    ]