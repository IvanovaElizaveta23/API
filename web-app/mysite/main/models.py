from urllib import request

from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()
    quantity=models.IntegerField()
    photo=models.ImageField(upload_to='')
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

