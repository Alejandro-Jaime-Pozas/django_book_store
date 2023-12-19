from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# django.db.models.Model contains all the sql needed to create models
class Book(models.Model):
    # django auto-creates the primary ID
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # to only allow certain values
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # create slug format like lord-of-the-rings; can improve field searches by setting index to True (db_index=True); editable=False does not allow admin user to edit this field

    # allows to get a url that represents each instance of this Book model
    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug]) # pass id into args
    
    # # don't need this below since we're already in admin.py securely adding a slug value and accounting for it being a valid value
    # # this below save() overrides the original method, so always include params from original
    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs) # fwd all args and kwargs from new method to original save method

    def __str__(self) -> str:
        return f"{self.title} - by {self.author} ({self.rating})"
