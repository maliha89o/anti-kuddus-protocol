from django.urls import path
from . import views

urlpatterns = [
    path('', views.fact_checker, name='fact_checker'),
]