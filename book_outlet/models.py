from django.db import models

# Create your models here.

# django.db.models.Model contains all the sql needed to create models
class Book(models.Model):
    # django auto-creates the primary ID
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    