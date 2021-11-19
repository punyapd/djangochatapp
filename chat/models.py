from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100000)


class Message(models.Model):
    msg = models.CharField(max_length=1000000)
    date =models.DateTimeField(default=datetime.now)
    room = models.CharField(max_length=100000)
    msg_user = models.CharField(max_length=10000)

