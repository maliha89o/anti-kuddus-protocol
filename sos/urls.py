from django.urls import path
from . import views

urlpatterns = [
    path('', views.trigger_sos, name='trigger_sos'),
    path('api/create/', views.create_sos_alert, name='create_sos_alert'),
    path('dashboard/', views.captain_dashboard, name='captain_dashboard'),
    path('api/active/', views.get_active_alerts, name='get_active_alerts'),
    path('api/resolve/<int:alert_id>/', views.resolve_alert, name='resolve_alert'),
]