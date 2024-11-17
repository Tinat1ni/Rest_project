from django.db import models
# from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    cover_picture = models.ImageField(upload_to='images/', null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MainMenuCategory(models.Model):
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
    cover_photo = models.ImageField(upload_to='images/', null=True, blank=True,)
    parent_category = models.ForeignKey(MainMenuCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/', null=True, blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    menu_sub_category = models.ForeignKey(Subcategory, related_name='meals', on_delete=models.CASCADE)

    def __str__(self):
        return self.name