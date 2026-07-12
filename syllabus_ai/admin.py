

from django.contrib import admin
from .models import SyllabusRequest, CurriculumTopic


@admin.register(SyllabusRequest)
class SyllabusRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(CurriculumTopic)
class CurriculumTopicAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'topic', 'is_examinable')
    list_filter = ('chapter', 'is_examinable')