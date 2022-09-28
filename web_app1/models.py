from datetime import date
from django.db import models


class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Animal_data(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=date.today)
