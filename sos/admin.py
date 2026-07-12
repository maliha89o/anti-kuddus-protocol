from django.contrib import admin
from .models import SOSAlert


@admin.register(SOSAlert)
class SOSAlertAdmin(admin.ModelAdmin):
    list_display = ('location', 'triggered_at', 'resolved', 'synced_from_offline')
    list_filter = ('location', 'resolved')