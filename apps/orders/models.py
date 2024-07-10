from django.db import models

from apps.cinemas.models import Session, Place
from apps.users.models import User


class Order(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             null=True,
                             on_delete=models.SET_NULL)
    session = models.ForeignKey(Session,
                                verbose_name='Сеанс',
                                null=True,
                                on_delete=models.SET_NULL)
    place = models.ForeignKey(Place,
                              verbose_name='Место',
                              null=True,
                              on_delete=models.SET_NULL)
    date_create = models.DateTimeField(verbose_name='Дата создания', 
                                       auto_now=True)
    active = models.BooleanField(verbose_name='Активный', default=False)
    scanned = models.BooleanField(verbose_name='Отсканированный', default=False)

    def __str__(self) -> str:
        return f'Заказ на имя {self.user}'
