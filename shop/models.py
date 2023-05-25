from django.db import models
from django.conf import settings
# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField('Nom du produit', max_length=200)
    price = models.DecimalField('Prix', max_digits=10, decimal_places=2)
    image = models.ImageField('Illustration', upload_to='product_images/')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"



