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
    genre = models.CharField(verbose_name='Жанр', 
                             max_length=128, 
                             null=True, 
                             blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Cinema(models.Model):
    name = models.CharField(verbose_name='Название')
    picture = models.ImageField(verbose_name='Фото',
                                null=True,
                                blank=True,
                                upload_to=upload_instance_image)
    address = models.CharField(verbose_name='Адрес')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class Hall(models.Model):
    name = models.CharField(verbose_name='Название')
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               related_name='cinema',
                               on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Row(models.Model):
    number = models.IntegerField(verbose_name='Ряд')
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               on_delete=models.CASCADE,
                               null=True)
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
        return f'Ряд номер {self.number}'
    
    class Meta:
        verbose_name = 'Ряд'
        verbose_name_plural = 'Ряды'


# cinema = models.ForeignKey(Cinema,
#                                verbose_name='Кинотеатр',
#                                on_delete=models.CASCADE,
#                                null=True)
# hall = ChainedForeignKey(
#     Hall,
#     verbose_name='Зал',
#     chained_field="cinema",
#     chained_model_field="cinema",
#     show_all=False,
#     auto_choose=True,
#     default=None,
#     sort=True
# )
# row = ChainedForeignKey(
#     Row,
#     verbose_name='Ряд',
#     chained_field="hall",
#     chained_model_field="hall",
#     show_all=False,
#     auto_choose=True,
#     default=None,
#     sort=True
# )

class Place(models.Model):
    number = models.IntegerField(verbose_name='Место')
    cinema = models.ForeignKey(Cinema,
                               verbose_name='Кинотеатр',
                               on_delete=models.CASCADE,
                               null=True)
    hall = ChainedForeignKey(
        Hall,
        verbose_name='Зал',
        chained_field="cinema",
        chained_model_field="cinema",
        show_all=False,
        auto_choose=True,
        default=None,
        sort=True,
        null=True,
    )
    row = ChainedForeignKey(
        Row,
        verbose_name='Ряд',
        chained_field="hall",
        chained_model_field="hall",
        show_all=False,
        auto_choose=True,
        default=None,
        sort=True,
        null=True,
    )  

    def __str__(self) -> str:
        return f'Место номер {self.number}'
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


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

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'