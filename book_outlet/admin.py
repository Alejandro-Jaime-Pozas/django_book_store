from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

# this class added manually
# this class allows for modification of django admin site
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',) # must include a tuple or list for read-only fields
    prepopulated_fields = {'slug': ('title', )} # allows for real-time text updates
    list_filter = ('author', 'rating', ) # this allows for filtering on admin site
    list_display = ('title', 'author', ) # allows for columns when displaying objects

admin.site.register(Book, BookAdmin) # this tells Django to ADD this model to the admin site, and that BookAdmin class is linked to the Book class
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)