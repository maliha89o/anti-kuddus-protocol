from django.contrib import admin
from .models import SchoolRule


@admin.register(SchoolRule)
class SchoolRuleAdmin(admin.ModelAdmin):
    list_display = ('category', 'rule_text')
    list_filter = ('category',)