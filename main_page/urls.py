from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name='films_list'),
    path('film_detail/<int:id>/', views.FilmDetailView.as_view(), name='detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]
