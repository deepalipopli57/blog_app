from django.db import models

# Create your models here.
from django.forms import ModelForm


class BlogsModel(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='static', blank=True)

    def __str__(self):
        return (self.title)

