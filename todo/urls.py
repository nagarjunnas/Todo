from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.home, name='home'),
    path('add-todo', views.add_todo, name='add_todo'),
    path('in-progress', views.in_progress, name='progress'),
    path('completed', views.completed, name='completed'),
    path('pending', views.pending, name='pending'),
    path('edit/<int:todo_id>', views.edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('todos', api.todos, name='todos'),
    path('todo/<int:todo_id>', api.todo, name='todo'),
]