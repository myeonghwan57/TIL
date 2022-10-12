from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# from .models import User 
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            #세션에 저장 
            # login 함수에서는 request,user 객체를 인자로 받음
            # user 객체는 바로 form 에서 인증된 유저 
            auth_login(request, form.get_user())

            return redirect( request.GET.get('next') or'articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form' : form,
    }
    return render (request, 'accounts/login.html',context)