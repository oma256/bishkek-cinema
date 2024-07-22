from django.urls import path

from apps.orders.views import order_request


app_name = 'orders'

urlpatterns = [
    path('request/', order_request, name='order_request')
]
