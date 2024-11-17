from django_filters.rest_framework import FilterSet, filters
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Subcategory, Restaurant, MainMenuCategory, Meal
from .serializers import SubcategorySerializer, RestaurantSerializer, MainMenuCategorySerializer, \
    SubcategoryDetailSerializer, MealSerializer


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SubcategoryFilter(FilterSet):
    parent_category = filters.CharFilter(field_name='parent_category__name', lookup_expr='icontains')
    meal_name = filters.CharFilter(field_name='meals__name', lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Subcategory
        fields = ['parent_category', 'meal_name', 'name']


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.select_related('parent_category')
    serializer_class = SubcategorySerializer
    filter_class = SubcategoryFilter
    pagination_class = PageNumberPagination


class SubcategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.prefetch_related('meals')
    serializer_class = SubcategoryDetailSerializer


class MealsListAPIView(generics.ListAPIView):
    queryset = Meal.objects.select_related('menu_sub_category')
    serializer_class = MealSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'menu_sub_category__name']


class RestaurantCreateAPIView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MainMenuCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = MainMenuCategory.objects.select_related('restaurant')
    serializer_class = MainMenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        if restaurant_id:
            return MainMenuCategory.objects.filter(restaurant_id=restaurant_id)
        return MainMenuCategory.objects.all()


    def perform_create(self, serializer):
        restaurant_id = self.kwargs.get('restaurant_id')
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            raise NotFound(detail='restaurant with that id does not exist')

        serializer.save(restaurant=restaurant)

