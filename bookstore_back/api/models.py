from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)

    def __str__(self):
        return self.title

