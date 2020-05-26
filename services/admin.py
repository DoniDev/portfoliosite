from django.contrib import admin
from . models import Service, Introduction

admin.site.register(Introduction)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    list_filter = ['name','icon']
    search_fields = ['name', 'icon']

