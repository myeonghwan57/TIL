from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# from django.contrib.auth.forms import UserCreationForm
# from .models import User
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 로그인
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    # user = get_user_model().objects.get(pk=pk)
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수에서는 request,user 객체를 인자로 받음
            # user 객체는 바로 form 에서 인증된 유저
            auth_login(request, form.get_user())

            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    messages.warning(request, "로그아웃 하였습니다.")
    return redirect("articles:index")


@login_required
def update(request):
    # 유효성 검사
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    # 스스로를 팔로우하려는 경우
    if request.user == user:
        messages.warning(request, "스스로 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    # 팔로우하고 있는 상태인 경우
    if request.user in user.folloewers.all():
        user.followers.remove(request.user)
    # 팔로우하고 있지 않았을때
    else:
        user.followers.add(request.user)
    return redirect("accounts:detail", pk)
