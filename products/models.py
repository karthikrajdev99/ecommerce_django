from django.db import models
from django.urls import reverse
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary

from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={"name": self.name})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, default="Empty description.")
    picture = CloudinaryField('picture', null=True ,blank=True, chunk_size=1000000)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)  
    featured = models.BooleanField(default=False) 

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0

# @receiver(pre_delete, sender=Product)
# def picture_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.picture.public_id)