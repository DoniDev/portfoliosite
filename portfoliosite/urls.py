from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

admin.site.site_header = 'DoniDev Portfolio Admin'

admin.site.site_title = 'DoniDev'

admin.site.index_title = "My personal portfolio site admin"