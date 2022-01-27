from dataclasses import field
from django.contrib import admin
from .models import (
    Department, Lectures, Subjects
)


admin.site.register(Department)
# admin.site.register(Subjects)
# admin.site.register(Lectures)

@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):

    fields = ('subject', 'department')
    list_display = ('subject', 'department')
    list_display_links = ('subject',)
    search_fields = ('subject', 'department')
    list_filter = ('subject', 'department')
    # list_editable = ('subject', 'department')


@admin.register(Lectures)
class LectureAdmin(admin.ModelAdmin):

    fields = ('lecture', 'lecture_number', 'lecture_teacher', 'subject')
    list_display = ('lecture', 'lecture_number', 'lecture_teacher', 'subject')
    list_display_links = ('lecture',)
    search_fields = ('lecture', 'lecture_number', 'lecture_teacher')
    list_filter = ('subject',)
    # list_editable = ('lecture', 'lecture_number', 'lecture_teacher', 'subject')
    