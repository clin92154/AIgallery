from django.db import models
from django import forms
# Create your models here.
class MakerSpace(models.Model):
    prompt = models.CharField(max_length=255)  #prompt
    