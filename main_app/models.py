from django.db import models
from django.utils.safestring import mark_safe

class Appartment(models.Model):
    address = models.CharField(max_length=300, verbose_name="Адрес")
    rooms = models.PositiveIntegerField(verbose_name="Количество комнат")
    floor = models.PositiveIntegerField(verbose_name="Этаж")
    sleeping_place = models.CharField(verbose_name="Количество спальных мест", max_length=100)
    price = models.PositiveIntegerField(verbose_name="Цена за сутки")
    descriptiion = models.TextField(max_length=2500, verbose_name="Описание", default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = "Аппартаменты"
        verbose_name_plural = "Аппартаменты"

class AppartmentImage(models.Model):
    photo = models.ImageField(verbose_name="Фото")
    appartment = models.ForeignKey(Appartment, verbose_name="Аппартаменты", on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def image_preview(self):
        if self.photo:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.photo.url))
        else:
            return '(No image)'

class Application(models.Model):
    address = models.CharField(max_length=300, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    date_start = models.DateTimeField(verbose_name="Дата заезда", blank=True, default=None, null=True)
    date_end = models.DateTimeField(verbose_name="Дата выезда", blank=True, default=None, null=True)

    class Meta():
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"