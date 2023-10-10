from django.db import models
from app_User.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self):
        return self.name

# class Type(models.Model):
#     name = models.CharField(max_length=1024,unique=True)
#
#     def __str__(self):
#         return self.name

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=1024)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.id)