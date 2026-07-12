from django.contrib import admin

from django.contrib import admin
from .models import Complaint, RollNumberHash


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('category', 'submitted_at', 'is_verified_strike')
    list_filter = ('category', 'is_verified_strike')
    readonly_fields = ('submitted_at',)


@admin.register(RollNumberHash)
class RollNumberHashAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    readonly_fields = ('hashed_roll', 'created_at')
