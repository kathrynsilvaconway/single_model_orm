from django.db import models
from django.db.models.fields import DateTimeField

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at=DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_now=True)


# Create your models here.
