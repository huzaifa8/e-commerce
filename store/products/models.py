from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name




