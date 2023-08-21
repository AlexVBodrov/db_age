from django.db import models
from market_dashbord.models import Market
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLE = (
        ('SV', 'Super Visor'),
        ('M', 'Manager'),
        ('SS', 'senior sales'),
        ('W', 'worker'),
    )
    # REQUIRED_FIELDS
    position = models.CharField(
        verbose_name='Должность', max_length=2, choices=ROLE)
    telephone = models.CharField(verbose_name='Телефон', unique=True, max_length=18, error_messages={
                                 'unique': 'Пользователь с таким telephone уже есть'})
    email = models.EmailField(verbose_name='E-mail',
                              unique=True,
                              blank=False,
                              error_messages={
                                  'unique': 'Пользователь с таким email уже есть'}
                              )

    market_number = models.ForeignKey(Market, on_delete=models.SET_NULL, verbose_name='Номер магазина', blank=True,
                                      null=True)
    avatar = models.ImageField(
        upload_to='users_avatars/%Y-%m-%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        # если поля заполнены
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username
