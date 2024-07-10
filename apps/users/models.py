from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    phone_number = models.CharField(
        verbose_name='Номер телефона', max_length=20, unique=True,
    )
    email = models.EmailField(verbose_name='Почта', unique=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    date_joined = models.DateTimeField(
        verbose_name='Зарегестрирован', default=timezone.now,
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        full_name = ''

        if self.last_name:
            full_name += self.last_name
        if self.first_name:
            full_name += f' {self.first_name}'

        return full_name

    @property
    def get_first_name(self):
        return self.first_name