from django.db import models
from market_dashbord.models import Market
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # REQUIRED_FIELD
    telephone = models.CharField(verbose_name='telephone', max_length=12, error_messages={
                                 'unique': 'Пользователь с таким telephone уже есть'})

    email = models.EmailField(verbose_name='email',
                              unique=True,
                              blank=False,
                              error_messages={
                                  'unique': 'Пользователь с таким email уже есть'}
                              )


class UserProfile(User):
    ROLE = (
        ('SV', 'Super Visor'),
        ('M', 'Manager'),
        ('SS', 'senior sales'),
        ('W', 'worker'),
    )
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='users_avatars/%Y-%m-%d/', blank=True, verbose_name='avatar')
    age = models.PositiveIntegerField(
        verbose_name='возраст', blank=False, default=18)
    position = models.CharField(max_length=2, choices=ROLE)
    number_market = models.ForeignKey(
        Market, on_delete=models.CASCADE)
    # custom

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username
