# Generated by Django 3.2.18 on 2023-07-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('number_market', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('adress_market', models.CharField(max_length=65, unique=True)),
            ],
        ),
    ]
