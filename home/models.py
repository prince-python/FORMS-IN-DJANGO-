from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    passord= models.CharField(max_length=100)
    
