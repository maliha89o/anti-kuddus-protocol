from django.urls import path
from . import views

urlpatterns = [
    path('', views.syllabus_negotiator, name='syllabus_negotiator'),
]