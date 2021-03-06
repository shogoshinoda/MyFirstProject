# Generated by Django 3.2.9 on 2022-01-13 06:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_picture', models.FileField(upload_to='boards/')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('boards_picture', models.FileField(null=True, upload_to='boards/')),
                ('description', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2022, 1, 13, 15, 25, 13, 9973))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2022, 1, 13, 15, 25, 13, 9982))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'boards',
            },
        ),
    ]
