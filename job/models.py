from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Job(models.Model):
    username = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2500)

    def get_absolute_url(self):
        return reverse('job:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username+ '-' + self.title + '-' + self.description