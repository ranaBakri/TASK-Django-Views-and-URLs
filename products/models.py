from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}, {self.price}KD , {self. description}"
