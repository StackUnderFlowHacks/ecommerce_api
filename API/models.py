from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(help_text='Name of product', max_length=200)
    price = models.PositiveIntegerField(help_text='Price of Product', default=0)
    manufacturer = models.CharField(help_text='Name of manufacturer', max_length=200, default='')
    thumbnails = models.CharField(help_text='Paste link of thumbnail photo', max_length=100, default='', blank=True)
    stock = models.PositiveBigIntegerField(help_text='Available quantity of product', default=0)
    isInStock = models.BooleanField(help_text='is product available for purchases?', default=False)
    paymentOption = models.CharField(help_text="What's the payment options available on product", max_length=100,
                                     default='Cash On Delivery (C.O.D.)')

    def __str__(self):
        return f"{self.productId} - {self.name}"


class ProductDetails(models.Model):
    product_id = models.OneToOneField(Product, help_text='Select product ID', on_delete=models.CASCADE,
                                      primary_key=True)
    description = models.TextField(help_text='Description of the product', default='')
    countryOfOrigin = models.CharField(help_text="What's the Country of Origin", max_length=20, default=None)
    photos = ArrayField(models.CharField(max_length=450, default=None), blank=True, default=None,
                        help_text="Paste links for the photos of products separated by commas")
    categories = ArrayField(models.CharField(max_length=20, default=None), blank=True, default=None,
                            help_text="Define category of product")
    rating = models.DecimalField(decimal_places=1, max_digits=5, blank=True, help_text="rating out of 5")
    discount = models.DecimalField(decimal_places=2, max_digits=12, blank=True,
                                   help_text="how much discount is ongoing for product (in %)")
    coupons = ArrayField(models.CharField(max_length=20, default=None), default=None, blank=True,
                         help_text="coupon codes for this product separated by commas")

    def __str__(self):
        return f"{self.product_id.productId} - {self.product_id.name}"
