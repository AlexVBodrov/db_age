# Generated by Django 3.2.18 on 2023-08-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20230821_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким telephone уже есть'}, max_length=18, unique=True, verbose_name='Телефон'),
        ),
    ]
