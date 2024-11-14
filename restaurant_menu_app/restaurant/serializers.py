from rest_framework import serializers
from .models import Restaurant, Menu, Ingredient, Subcategory, Meal

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    parent_category = MenuSerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    menu_sub_category = SubcategorySerializer(read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'




