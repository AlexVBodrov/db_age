# Generated by Django 3.2.18 on 2023-08-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
