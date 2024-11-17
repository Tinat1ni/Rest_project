from django.urls import path

from .views import RestaurantListAPIView, MainMenuCategoryListAPIView, SubCategoryListAPIView, \
    SubcategoryDetailAPIView, MealsListAPIView, MainMenuCategoryCreateAPIView

app_name='restaurant'
urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view(), name = 'restaurant_listing'),
    path('main-menu-categories/<int:restaurant_id>', MainMenuCategoryListAPIView.as_view(), name='main_menu_categories'),
    path('sub-category', SubCategoryListAPIView.as_view(), name='subcategory_listing'),
    path('subcategory/<int:pk>/', SubcategoryDetailAPIView.as_view(), name='subcategory-detail'),
    path('meals/', MealsListAPIView.as_view(), name='meals-list'),
    path('main-menu-category/create', MainMenuCategoryCreateAPIView.as_view(), name='create_menu')
]