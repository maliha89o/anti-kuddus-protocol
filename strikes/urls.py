from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.roll_login, name='roll_login'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('dashboard/', views.dashboard, name='dashboard'),
]