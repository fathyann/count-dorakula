from django.db import models

# Create your models here.
class Queue(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)

class Retry(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)

class Top(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)
