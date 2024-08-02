from django.db import models

from apps.cinemas.models import Cinema, Hall, Row, Session, Place
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
    row = models.ForeignKey(Row,
                            verbose_name='Ряд',
                            null=True,
                            on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall,
                             verbose_name='Зал',
                             null=True,
                             on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               null=True,
                               on_delete=models.CASCADE)
    date_create = models.DateTimeField(verbose_name='Дата создания', 
                                       auto_now=True)
    active = models.BooleanField(verbose_name='Активный', default=False)
    scanned = models.BooleanField(verbose_name='Отсканированный', default=False)
    booked = models.BooleanField(verbose_name='Забронирован', default=True)

    def __str__(self) -> str:
        return f'Заказ на имя {self.user}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
