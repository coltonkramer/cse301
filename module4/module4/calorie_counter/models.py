import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Foods(models.Model):
     food = models.CharField(default="pizza", max_length=100)
     calories = models.CharField(default="100", max_length=5)

     def __str__(self):
          return self.food.title()