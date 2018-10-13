from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Todo

def todos(request):
    todos = Todo.objects.all()
    data = [{
        'title': todo.title, 
        'description': todo.description,
        'status': todo.status.title().replace('_', ' '),
        'created_date_time': todo.created_date_time,
        'created_at': todo.created_at,
        'modified_at': todo.modified_at,
    } for todo in todos]
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})     


def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    data = {
        'title': todo.title, 
        'description': todo.description,
        'status': todo.status.title().replace('_', ' '),
        'created_date_time': todo.created_date_time,
        'created_at': todo.created_at,
        'modified_at': todo.modified_at,
    }
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})