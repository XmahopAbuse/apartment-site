# Generated by Django 3.2.9 on 2021-12-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartment',
            name='show_in_main',
            field=models.BooleanField(default=False, verbose_name='Отображать на главной'),
        ),
    ]
