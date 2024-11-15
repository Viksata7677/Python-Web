from django.contrib import admin
from UrlsAndViews.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass