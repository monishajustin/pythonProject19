from django.db import models

# Create your models here.
class Form(models.Model):
    username=models.CharField(max_length=20)
    mobile=models.IntegerField()
    address=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Login(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    type = models.IntegerField()
class Product(models.Model):
    number=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    des=models.CharField(max_length=250)
    img=models.FileField()