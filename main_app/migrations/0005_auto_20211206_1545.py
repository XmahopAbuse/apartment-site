# Generated by Django 3.2.9 on 2021-12-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_application_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_end',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='application',
            name='date_start',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата заезда'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='Имя'),
        ),
    ]