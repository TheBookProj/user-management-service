from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True)
    email = models.CharField(unique=True)