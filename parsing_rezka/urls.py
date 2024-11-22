from django.urls import path
from . import views

urlpatterns = [
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list'),
    path('rezka_parser/', views.RezkaFormView.as_view(), name='rezka_parser'),
]
