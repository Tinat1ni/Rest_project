from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    cover_picture = VersatileImageField(upload_to='images/', null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    cover_photo = VersatileImageField(upload_to='images/', null=True, blank=True,)
    parent_category = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    photo = VersatileImageField(upload_to='images/', null=True, blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    menu_sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name