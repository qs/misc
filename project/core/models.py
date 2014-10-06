from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=200)


class TimeUnit(models.Model):
    activity = models.ForeignKey('Activity')
    name = models.CharField(max_length=200)
    dt_start = models.DateTimeField()
    dt_finish = models.DateTimeField()