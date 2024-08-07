from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.cinemas.urls')),
    path('orders/', include('apps.orders.urls')),
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('users/', include('apps.users.urls')),

    path('api/v1/', include('apps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
