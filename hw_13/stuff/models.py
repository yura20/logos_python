from django.db import models

# Create your models here.
class Stuff(models.Model):
    name = models.CharField(
        max_length = 255,
    )
    description = models.TextField()
    category = models.CharField(
        max_length = 255,
    )
    price = models.FloatField()
    amount_of_stuff = models.IntegerField()
    discount_status = models.BooleanField(
        default = False,
    )
    discount = models.FloatField()

class Review(models.Model):
    name = models.CharField(
        max_length = 255,
    )
    email = models.EmailField()
    review = models.TextField()
    