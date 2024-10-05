from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm


# 顯示代辦事項
def todo_list(request):
    todos = None
    user = request.user
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_one(request, id):
    msg = ""
    todo = None
    user = request.user
    try:
        todo = Todo.objects.get(id=id, user=user)
        form = TodoForm(instance=todo)
    except Exception as e:
        print(e)
        msg = "id/user error!"
    return render(request, "todo/todo.html", {"form": form, "todo": todo, "msg": msg})


# 新增代辦事項
def creat_todo_form(request):
    msg = ""
    form = None
    user = request.user
    if not user.is_authenticated:
        msg = "please login first"
    else:
        form = TodoForm()
        if request.method == "POST":
            try:
                form = TodoForm(request.POST)
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                msg = "success!"
                return redirect("todo_list")
            except Exception as e:
                print(e)
                msg = "creat_todo error!"

    return render(request, "todo/creat-todo.html", {"form": form, "msg": msg})
