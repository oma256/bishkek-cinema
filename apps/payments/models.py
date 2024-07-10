from django.db import models

from apps.orders.models import Order


class Transfer(models.Model):
    order = models.ForeignKey(Order,
                              verbose_name='Заказ',
                              null=True,
                              on_delete=models.SET_NULL)
    amount = models.IntegerField(verbose_name='Сумма')
    status = models.CharField(verbose_name='Статус')
