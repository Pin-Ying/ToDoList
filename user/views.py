from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        elif password1 != password2:
            msg = "兩次密碼不相同"

        else:
            # 帳號是否存在
            if User.objects.filter(username=username):
                msg = "帳號已存在"

            # 註冊使用者
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                msg = "註冊成功"
    return render(request, "user/register.html", {"form": form, "msg": msg})
