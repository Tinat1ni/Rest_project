from rest_framework import serializers
from .models import Restaurant, MainMenuCategory, Ingredient, Subcategory, Meal

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class MainMenuCategorySerializer(serializers.ModelSerializer):
    # restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = MainMenuCategory
        fields = ['id', 'name']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    parent_category = MainMenuCategorySerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id','name', 'cover_photo', 'parent_category']


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    menu_sub_category = SubcategorySerializer(read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'


class SubcategoryDetailSerializer(serializers.ModelSerializer):
     meals = MealSerializer(many=True)

     class Meta:
         model = Subcategory
         fields = ['id', 'name', 'cover_photo', 'meals']


