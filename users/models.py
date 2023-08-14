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
        verbose_name='position', max_length=2, choices=ROLE)
    telephone = models.CharField(verbose_name='telephone', unique=True, max_length=11, error_messages={
                                 'unique': 'Пользователь с таким telephone уже есть'})
    email = models.EmailField(verbose_name='email',
                              unique=True,
                              blank=False,
                              error_messages={
                                  'unique': 'Пользователь с таким email уже есть'}
                              )

    market_number = models.ForeignKey(Market, on_delete=models.SET_NULL, verbose_name='market_number', blank=True,
                                      null=True)
    avatar = models.ImageField(
        upload_to='users_avatars/%Y-%m-%d/', blank=True, verbose_name='avatar')

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username
