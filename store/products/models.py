from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name







