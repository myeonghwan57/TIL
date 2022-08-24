from django.db import models
class Director(models.Model):
    name = models.TextField()
    debut = models.DateField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()