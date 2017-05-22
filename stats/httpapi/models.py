from django.db import models

# Create your models here.

class Acter(models.Model):
    name = models.CharField(max_length=100)


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    acters = models.ManyToManyField(Acter)
    count_users = models.IntegerField(default=0)
    watch_time = models.FloatField(default=0.0)


class Stats(models.Model):
    customer = models.IntegerField()
#    film = models.ForeignKey(Film)
    film = models.CharField(max_length=100)
    watch_start = models.DateTimeField()
    watch_end = models.DateTimeField()
