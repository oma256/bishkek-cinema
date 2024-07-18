from django.db import models

from utils.image_upload import upload_instance_image
from smart_selects.db_fields import ChainedForeignKey


class Movie(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    country = models.CharField(verbose_name='Страна', max_length=128)
    year = models.CharField(verbose_name='Год', max_length=4)
    duration = models.IntegerField(verbose_name='Продолжительность')
    starring = models.TextField(verbose_name='В главных ролях')
    picture = models.ImageField(verbose_name='Постер',
                                upload_to=upload_instance_image,
                                null=True,
                                blank=True)

    def __str__(self) -> str:
        return self.name


class Cinema(models.Model):
    name = models.CharField(verbose_name='Название')
    picture = models.ImageField(verbose_name='Фото',
                                null=True,
                                blank=True,
                                upload_to=upload_instance_image)
    address = models.CharField(verbose_name='Адрес')

    def __str__(self) -> str:
        return self.name


class Hall(models.Model):
    name = models.CharField(verbose_name='Название')
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               related_name='cinema',
                               on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Row(models.Model):
    number = models.IntegerField(verbose_name='Ряд')
    hall = models.ForeignKey(Hall,
                             verbose_name='Зал',
                             related_name='hall',
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Ряд номер {self.number}'
    

class Place(models.Model):
    number = models.IntegerField(verbose_name='Место')
    row = models.ForeignKey(Row,
                            verbose_name='Ряд',
                            related_name='row',
                            on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Место номер {self.number}'
    

class Session(models.Model):
    start_time = models.DateTimeField(verbose_name='Время')
    price = models.IntegerField(verbose_name='Цена')
    movie = models.ForeignKey(Movie,
                              verbose_name='Фильм',
                              on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               on_delete=models.CASCADE)
    hall = ChainedForeignKey(
        Hall,
        verbose_name='Зал',
        chained_field="cinema",
        chained_model_field="cinema",
        show_all=False,
        auto_choose=True,
        default=None,
        sort=True
    )

    def __str__(self) -> str:
        return f'Сеанс начало в {self.start_time}, цена {self.price}'
