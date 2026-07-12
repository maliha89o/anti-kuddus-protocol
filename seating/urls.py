from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('generate/', views.generate_seating_view, name='generate_seating'),
]