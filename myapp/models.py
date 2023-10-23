
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
class shoes(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="media/",unique=True)
    description=models.TextField()
    price=models.IntegerField()
    def __str__(self):
        return self.name;
# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=254, unique=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name

    
