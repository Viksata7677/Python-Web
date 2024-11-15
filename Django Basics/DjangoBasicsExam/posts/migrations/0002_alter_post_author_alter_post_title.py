# Generated by Django 5.1.2 on 2024-10-27 12:16

import django.db.models.deletion
import posts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_first_name_alter_author_last_name_and_more'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='author.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'unique': 'Oops! That title is already taken. How about something fresh and fun?'}, max_length=50, unique=True, validators=[posts.models.validate_title_length]),
        ),
    ]
