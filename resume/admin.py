from django.contrib import admin
from . models import Field, Activity

@admin.register(Activity)
class ActtivityAdmin(admin.ModelAdmin):
    list_display = ['field', 'duration', 'job', 'location']


admin.site.register(Field)
