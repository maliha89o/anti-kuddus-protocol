from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_transaction, name='log_transaction'),
    path('dashboard/', views.economy_dashboard, name='economy_dashboard'),
]