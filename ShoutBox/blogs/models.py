from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class posts(models.Model):
    
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return f'{self.author}'



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    published_on = models.DateField()

    @property
    def is_in_stock(self):
        return self.quantity > 0