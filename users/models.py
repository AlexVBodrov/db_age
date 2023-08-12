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

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username


# class UserProfile(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(
#         upload_to='users_avatars/%Y-%m-%d/', blank=True, verbose_name='avatar')
#     age = models.PositiveIntegerField(
#         verbose_name='возраст', blank=False, default=18)

#     number_market = models.ForeignKey(
#         Market, on_delete=models.CASCADE)
#     # custom

#     def __str__(self):
#         return self.username
