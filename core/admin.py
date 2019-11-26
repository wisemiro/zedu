# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Category, Chapter, CourseItem

# Register your models here.

admin.register(Category, Chapter, CourseItem)(admin.ModelAdmin)
