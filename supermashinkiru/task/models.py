from django.db import models
from race.models import Race
from race.models import ExtendUser


class Task(models.Model):
    "Модель задач"
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    number = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=50)
    text = models.TextField(null=True)


class Answer(models.Model):
    "Модель отправленных решений задач"
    user = models.ForeignKey(ExtendUser, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    text = models.TextField(null=True)
    date = models.DateField(auto_now=True)


class Comments(models.Model):
    "Модель комментариев проверяющего к отправленным решениям"
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
    text = models.TextField(null=True)
    view = models.BooleanField()
    accepted = models.BooleanField(default=False)
