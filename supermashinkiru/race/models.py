from django.db import models
from django.contrib.auth.models import User


class ExtendUser(models.Model):
    "Расширение модели User"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    phrase = models.CharField(max_length=100, default='')
    details = models.ManyToManyField('Details')


class Details(models.Model):
    "Модель деталей для машин"
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True)
    used = models.BooleanField(default=False)


class Car(models.Model):
    "Модель машин пользователей"
    user = models.OneToOneField(ExtendUser, on_delete=models.PROTECT)
    form = models.ForeignKey(Details, related_name='cars_form', on_delete=models.PROTECT)
    window = models.ForeignKey(Details, related_name='cars_window', on_delete=models.PROTECT)
    wheels = models.ForeignKey(Details, related_name='cars_wheels', on_delete=models.PROTECT)
    sticker = models.ForeignKey(Details, related_name='cars_sticker', on_delete=models.PROTECT)


class Race(models.Model):
    "Модель гонок"
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    length = models.SmallIntegerField(null=True)
    description = models.TextField(null=True)
    winner = models.ForeignKey(ExtendUser, null=True, on_delete=models.PROTECT)
    first_prize = models.ForeignKey(Details, related_name='race_first_prize', null=True, on_delete=models.PROTECT)
    prize = models.ForeignKey(Details, related_name='race_prize', null=True, on_delete=models.PROTECT)


class Racer(models.Model):
    "Модель участников гонок"
    user = models.ForeignKey(ExtendUser, on_delete=models.PROTECT)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    step = models.SmallIntegerField(null=True)