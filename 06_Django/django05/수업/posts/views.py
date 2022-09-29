from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다.
    # db에서 모든 글을 불러온다
    posts = Post.objects.all()
    # template 에 보내준다.
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):

    # parameter 로 날아온 데이터 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")
    # db에 저장
    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return redirect("posts:index")


def delete(request, pk):
    # pk 에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")


def detail(request, pk_):
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "posts/edit.html", context)


def update(request, pk):

    post = Post.objects.get(pk=pk)

    # parameter 로 날아온 데이터 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")
    # db에 저장
    post.title = title
    post.content = content
    post.save()

    return redirect("posts:detail", post.pk)
