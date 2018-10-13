from .models import Todo

def get_todos(status):
    todos = Todo.objects.filter(is_deleted=False, status=status)
    result = {
        'todos': todos
    }
    return result