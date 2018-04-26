# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestBlog(models.Model):
    author  = models.CharField(max_length=200,null=True)
    title   = models.CharField(max_length=500,unique=True)
    post    = models.TextField()

    def __str__(self):
        return self.title