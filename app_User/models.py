from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    username = models.CharField(max_length=1024, unique=True)
    password = models.CharField(max_length=1024, unique=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.username
