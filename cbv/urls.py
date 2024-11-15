from django.urls import path
from . import views

urlpatterns = [
    path('todo_class/', views.TodoListView.as_view(), name='todo_class_list'),
    path('todo_class/<int:id>/update/', views.UpdateTodoView.as_view(), name='update'),
    path('todo_class/<int:id>/delete/', views.DeleteTodoView.as_view(), name='delete'),
    path('/create_todo/', views.CreateTodoView.as_view(), name='create_todo'),

]