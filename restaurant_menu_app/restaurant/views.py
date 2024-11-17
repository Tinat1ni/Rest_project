from django_filters.rest_framework import FilterSet, filters
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Subcategory, Restaurant, MainMenuCategory, Meal
from .serializers import SubcategorySerializer, RestaurantSerializer, MainMenuCategorySerializer, \
    SubcategoryDetailSerializer, MealSerializer


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MainMenuCategoryListAPIView(generics.ListAPIView):
    queryset = MainMenuCategory.objects.all()
    serializer_class = MainMenuCategorySerializer


class SubcategoryFilter(FilterSet):
    parent_category = filters.CharFilter(field_name='parent_category__name', lookup_expr='icontains')
    meal_name = filters.CharFilter(field_name='meals__name', lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Subcategory
        fields = ['parent_category', 'meal_name', 'name']


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_class = SubcategoryFilter


class SubcategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.prefetch_related('meals')
    serializer_class = SubcategoryDetailSerializer


class MealsListAPIView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'subcategory__name']