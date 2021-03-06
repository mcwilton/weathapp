from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=25)
    period = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])

    class Meta:
        verbose_name_plural = 'weather'


class Temperature(models.Model):
    period = models.DateField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()


class Values(models.Model):
    min = models.IntegerField()
    max = models.IntegerField()
    ave = models.IntegerField()
    med = models.IntegerField()


class Humidity(models.Model):
    humidity = models.IntegerField()
