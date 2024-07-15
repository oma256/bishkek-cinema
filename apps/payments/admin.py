from django.contrib import admin

from .models import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['order', 'amount', 'status']
