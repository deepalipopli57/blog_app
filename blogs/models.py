from django.db import models

# Create your models here.
from django.forms import ModelForm


class BlogsModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='static', blank=True)


class BlogsForm(ModelForm):
    class Meta:
        model = BlogsModel
        fields = ['image']
