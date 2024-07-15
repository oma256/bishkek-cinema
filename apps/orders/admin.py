from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'session', 'place', 
                    'date_create', 'active', 'scanned']
