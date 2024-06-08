from django.contrib import admin
from .models import Teacher
from import_export.admin import ImportExportModelAdmin


class TeacherAdmin(ImportExportModelAdmin):
    list_display = ("firstName", "lastName", "email", "password")


admin.site.register(Teacher, TeacherAdmin)
