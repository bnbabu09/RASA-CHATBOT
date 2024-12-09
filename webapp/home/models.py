from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField, UUIDField
from django.db.models.lookups import In

# Create your models here.
class Menu(models.Model):
    dish_name = models.CharField(max_length=200)
    prep_time = models.IntegerField(default=5)
    price = models.IntegerField(default=0)

class restaurant(models.Model):
    ac1 = models.BooleanField(default=True)
    takeaway1 = models.BooleanField(default=True)
    special = models.ForeignKey(Menu, on_delete=models.CASCADE)
    wifi = models.BooleanField(default=True)
    payment = models.CharField(max_length=200)
    veg = models.BooleanField(default=True)
    can = models.BooleanField(default=True)
    washroom= models.BooleanField(default=True) 
    workinghours = models.CharField(max_length=200, default="10Am - 10PM")

class order(models.Model):
    amount = IntegerField(default=0)
    dish_name = models.CharField(max_length=200, default=None)
    spice = models.CharField(max_length=200, default=None)