from django.db import models

# Create your models here.
class User(models.model):
    Username = models.CharField(max_length=250)
    Password = models.CharField(max_length=20, Min_length=5)
    Email = models.CharField(max_length= 250)
    Contact_Number = models.IntegerField(max_Length= 12)

class Job(models.model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=250)
    Description = models.CharField(max_length=2500)
