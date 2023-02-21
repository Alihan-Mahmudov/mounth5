from django.contrib import admin
from Movie.models import Product, Director, Tag, Review

# Register your models here.

admin.site.register(Director)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Review)