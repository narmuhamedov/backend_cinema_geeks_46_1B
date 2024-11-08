from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products_list_view, name='all_products_tags'),
    path('drink_products/', views.drinks_list_view, name='drink_products_tags'),
    path('foods/', views.foods_list_view, name='foods_products_tags'),
]
