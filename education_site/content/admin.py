# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject, Article

admin.site.register(Subject)
admin.site.register(Article)
# Register your models here.
