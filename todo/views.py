from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from datetime import datetime


def todo_list(request):
    todos = None
    user = request.user
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_list_completed(request):
    todos = None
    user = request.user
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)
    return render(request, "todo/todo_list_completed.html", {"todos": todos})


# 顯示代辦事項
def todo_one(request, id):
    msg = ""
    todo = None
    user = request.user
    try:
        todo = Todo.objects.get(id=id, user=user)
        form = TodoForm(instance=todo)
        if request.method == "GET":
            form = TodoForm(instance=todo)
        else:
            form = TodoForm(request.POST, instance=todo)
            todo = form.save(commit=False)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            todo.date_completed = now if todo.completed else None
            todo.save()
            msg = "success!"
            return redirect("todo_list")
    except Exception as e:
        print(e)
        msg = "error!"
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
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                todo.date_completed = now if todo.completed else None
                todo.save()
                msg = "success!"
                return redirect("todo_list")
            except Exception as e:
                print(e)
                msg = "creat_todo error!"

    return render(request, "todo/creat-todo.html", {"form": form, "msg": msg})


# 刪除代辦事項
def delete_todo(request, id):
    msg = ""
    todo = None
    user = request.user
    try:
        todo = Todo.objects.get(id=id, user=user)
        todo.delete()
        return redirect("todo_list")
    except Exception as e:
        print(e)
        msg = "error!"
    return render(request, "todo/todo.html", {"msg": msg})
