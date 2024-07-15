from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.cinemas.urls')),
    path('admin/', admin.site.urls),
]
