from django.db import models


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField('Route', related_name='stations', blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Route(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
