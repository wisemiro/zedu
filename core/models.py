# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    image = models.ImageField(null=False)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(300, 300)],
                               format='JPEG',
                               options={'quality': 60})
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:Cat', kwargs={'slug': self.slug})


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name='chapter', null=False, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(null=False)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(500, 500)],
                               format='JPEG',
                               options={'quality': 60})

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:course_detail', kwargs={'slug': self.slug})


class CourseItem(models.Model):
    category = models.ForeignKey('Chapter', related_name='courseitem', default=1, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    lec_name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    video = models.FileField(upload_to='media/', max_length=100, blank=True)
    notes = models.FileField(upload_to='media/', max_length=100, blank=True)

    def __str__(self):
        return self.title
