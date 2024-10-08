"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("todo/<int:id>/", views.todo_one, name="todo_one"),
    path("creat-todo/", views.creat_todo_form, name="creat_todo"),
    path("delete-todo/<int:id>/", views.delete_todo, name="delete_todo"),
    path("todo-list-completed/", views.todo_list_completed, name="todo_list_completed"),
]
