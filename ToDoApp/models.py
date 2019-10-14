from django.db import models
from datetime import timedelta

# Create your models here.
from django.utils import timezone


class Importance(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256, unique=True)
    number = models.IntegerField(verbose_name='Порядковый номер', unique=True)


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256, unique=True)
    importance = models.ForeignKey(Importance, verbose_name='Важность', on_delete=models.SET_NULL, null=True)


class ToDoList(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата', default=timezone.now)
    importance = models.ForeignKey(Importance, verbose_name='Важность', on_delete=models.SET_NULL, null=True)


class Task(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    start_date = models.DateTimeField(verbose_name='Время начала', default=timezone.now)
    end_time = models.DateTimeField(verbose_name='Время конца', default=timezone.now() + timezone.timedelta(days=1))
    importance = models.ForeignKey(Importance, verbose_name='Важность', on_delete=models.SET_NULL, null=True)
    check = models.BooleanField(verbose_name='Статус завершения', default=False)
    to_do_list = models.ForeignKey(ToDoList, verbose_name='Список', on_delete=models.CASCADE)


