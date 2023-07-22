# Generated by Django 3.2.18 on 2023-06-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market_dashbord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('position', models.CharField(choices=[('M', 'Manager'), ('SS', 'senior sales'), ('W', 'worker')], max_length=2)),
                ('telephone', models.CharField(max_length=12)),
                ('e_mail', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('number_market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_dashbord.market')),
            ],
        ),
    ]
