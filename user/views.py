from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# from django.http import HttpResponse


def index(request):
    form = UserCreationForm()
    msg = ""
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 密碼長度至少8
        if len(password1) < 8 or len(password2) < 8:
            msg = "密碼長度不正確"

        # 密碼相同
        if password1 != password2:
            msg = "兩次密碼不相同"

        # 帳號是否存在

    return render(request, "user/register.html", {"form": form, "msg": msg})
