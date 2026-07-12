

from django.contrib import admin
from .models import Student, ClassroomLayout, SeatAssignment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'height_cm', 'needs_front_row')
    list_filter = ('needs_front_row',)
    search_fields = ('name', 'roll')


@admin.register(ClassroomLayout)
class ClassroomLayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'columns', 'aisle_after_column')


@admin.register(SeatAssignment)
class SeatAssignmentAdmin(admin.ModelAdmin):
    list_display = ('layout', 'student', 'row', 'column')
    list_filter = ('layout',)