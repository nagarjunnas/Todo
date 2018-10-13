# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .forms import TodoForm
from .models import Todo
from .helper import get_todos

# Create your views here.
def home(request):
	todos = Todo.objects.filter(is_deleted=False).filter(Q(status='in_progress') | Q(status='pending')).all()
	context = {
		'todos': todos
	}
	return render(request, 'index.html', context)


def in_progress(request):
    context = get_todos('in_progress')
    return render(request, 'index.html', context)


def completed(request):
    context = get_todos('completed')
    return render(request, 'index.html', context)


def pending(request):
    context = get_todos('pending')
    return render(request, 'index.html', context)


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'todo.html', {'form': form, 'action': 'Add'})


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.modified_at = timezone.now()
            todo.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo.html', {'form': form, 'action': 'Edit'})


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.modified_at = timezone.now()
    todo.is_deleted = True
    todo.save()
    return redirect('home')
