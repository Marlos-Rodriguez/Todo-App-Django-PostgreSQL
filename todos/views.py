from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import todos as Todo_model

# Create your views here.


def list_todo_items(request):

    todos = Todo_model.objects.all()

    context = {'todo_list': todos}

    return render(request, 'todos/todos_list.html', context)


def insert_todo_item(request: HttpRequest):

    if request.method == 'POST':
        todo = Todo_model(content=request.POST['content'])
        todo.save()

    return redirect('home')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo_model.objects.get(id=todo_id)

    todo_to_delete.delete()

    return redirect('home')
