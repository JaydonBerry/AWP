from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    contact =models.CharField(max_length=250)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('job:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title+ '-' + self.description + '-' + self.contact