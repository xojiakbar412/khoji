from django.db import models


# Create your models here.


class product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    published_at = models.DateTimeField(null=True)