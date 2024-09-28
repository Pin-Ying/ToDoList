from django.shortcuts import render
from .models import Todo
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    return render(request, "todo/todo_list.html", {"todos": todos})
