from django.contrib import admin

from . models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_of_birth', 'phone', 'address']
