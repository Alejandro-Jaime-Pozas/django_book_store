from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# django.db.models.Model contains all the sql needed to create models
class Book(models.Model):
    # django auto-creates the primary ID
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # to only allow certain values
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} - by {self.author} ({self.rating})"
