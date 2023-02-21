from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=500)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=500)
    movie = models.ForeignKey(Product, on_delete=models.CASCADE,
                                 related_name='product_review')
    stars = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    ), default=5)
    def __str__(self):
        return self.text


