from turtle import title
from django.db import models




class Product(models.Model):
    
    title = models.CharField(max_length=225)
    price = models.FloatField()
    discont_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title