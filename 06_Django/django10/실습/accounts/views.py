from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# from .models import User

from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == "POST":
        # form = UserCreationForm() -> 기본 제공해주는 form
        form = CustomUserCreationForm(request.POST)
        # 값이 유효하다면 저장 EX(비밀번호 완벽/ 아이디 중복 X)
        if form.is_valid():
            form.save()
            return redirect("articles:index")

    else:
        form = CustomUserCreationForm()
    # 유효하지 않는다면 다시 가입 페이지로 return
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    # 상속을 받고 있으니까
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)
