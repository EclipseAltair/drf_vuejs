# -*- coding: utf-8 -*-
from django.db import models


class Car(models.Model):
    vendor = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveIntegerField()

    def __str__(self):
        return str(self.vendor)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
