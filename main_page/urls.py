from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_list_view, name='films_list'),
    path('film_detail/<int:id>/', views.film_detail_view, name='detail'),
]
