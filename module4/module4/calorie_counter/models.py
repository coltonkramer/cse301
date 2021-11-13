from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Foods(models.Model):
     food = models.CharField(default="pizza", max_length=100)
     calories = models.CharField(default="100", max_length=5)
