from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_app/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
    return redirect('index')

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def toggle_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')
