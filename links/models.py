

# Create your models here.
from django.db import models

class Link(models.Model):
    link = models.URLField()
