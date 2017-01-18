from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    username = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2500)

    def __str__(self):
        return self.username+ '-' + self.title + '-' + self.description