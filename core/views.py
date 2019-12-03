# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Chapter, CourseItem
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView


# Create your views here.

"""Home view lists courses paginating them by 10 per page."""


class HomeView(ListView):
    model = Category
    paginate_by = 10
    template_name = "home.html"


"""
CatDetailView(DetailView) lists all the courses per category.
ie programming category includes java and python as a course
"""


class CatDetailView(DetailView):
    model = Category
    template_name = "subindex.html"


"""
this class provides a detail view of selected course
"""


class CourseDetailView(DetailView):
    model = Chapter
    template_name = "course-details.html"
    
    
"""
 this will only display ony a specific field in the courseitem model
"""   

class CourseItem(APIView):
    
    def get (self, request):
        path = str.split(str(request.path), '/')
        fieldname =path[2]
        if fieldname == 'title':
            content={'title' :title.objects.get(pk=path[1]).title}
            content = {
                    'fieldname': 'something',
                }
            return render (content, 'course-detail.html', request)