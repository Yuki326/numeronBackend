from django.db import models
from django.forms import IntegerField
from django.db import models

# Create your models here.

class Room(models.Model):
  code = models.CharField(max_length=4)
  num = models.IntegerField()
  start = models.DateTimeField(blank=True,null=True)


class Guess(models.Model):
  room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
  info = models.CharField(max_length=4)
  eat = models.IntegerField()
  bite = models.IntegerField()
  created_at = models.DateTimeField()