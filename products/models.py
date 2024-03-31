from django.db import models
from users.models import Users

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_img')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self.filter())

    def total_quantity(self):
        return sum(basket.quantity for basket in self.filter())



class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.product.price * self.quantity



