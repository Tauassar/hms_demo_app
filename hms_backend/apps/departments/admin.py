from django.contrib import admin

# Register your models here.
from apps.departments.models import Departments

admin.site.register(Departments)
