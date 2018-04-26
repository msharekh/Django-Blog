# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=500, unique=True)),
                ('post', models.TextField()),
            ],
        ),
    ]