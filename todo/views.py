from django.shortcuts import render
from .models import Todo
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def todo_list(request):
    todos = None
    user = request.user
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)
    print(todos)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_one(request, id):
    msg = ""
    todo = None
    user = request.user
    try:
        todo = Todo.objects.get(id=id, user=user)
    except Exception as e:
        print(e)
        msg = "id/user error!"
    return render(request, "todo/todo.html", {"todo": todo, "msg": msg})
