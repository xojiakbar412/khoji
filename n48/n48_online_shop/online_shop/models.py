
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    discount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price
        return self.price * (self.discount / 100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} {self.content[50]}"


class Order(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Order of {self.product_name} by {self.author} "