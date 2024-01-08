from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries" # this to change how it appears in admin site


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.postal_code}"
    
    # add a nested Meta class to access certain django Meta fields
    class Meta:
        verbose_name_plural = "Addresses" # this changes the plural output on admin site from 'Addresss' to 'Addresses'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


# django.db.models.Model contains all the sql needed to create models
class Book(models.Model):
    # django auto-creates the primary ID
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # to only allow certain values
    # # old way of just adding author as string vs object
    # author = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books') # foerign key
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # create slug format like lord-of-the-rings; can improve field searches by setting index to True (db_index=True); editable=False does not allow admin user to edit this field
    published_countries = models.ManyToManyField(Country, related_name='books') # can't add on_delete field for many to many relations, since would delete all connections bw them

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
