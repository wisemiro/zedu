from django.urls import path, include

from core.views import HomeView, CatDetailView,CourseDetailView
from . import views

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Category/<slug>/', CatDetailView.as_view(), name='Cat'),
    path('Course/<slug>/', CourseDetailView.as_view(), name='course_detail')
]
