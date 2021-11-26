# Generated by Django 3.2.9 on 2021-11-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211126_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('date_start', models.DateTimeField(blank=True, default=None, verbose_name='Дата заезда')),
                ('date_end', models.DateTimeField(blank=True, default=None, verbose_name='Дата выезда')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]