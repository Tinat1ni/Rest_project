from django.contrib import admin

from .models import Restaurant, MainMenuCategory, Ingredient, Subcategory, Meal

admin.site.register([Restaurant, MainMenuCategory, Ingredient, Subcategory, Meal ])
