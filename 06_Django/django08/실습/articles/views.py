from django.shortcuts import redirect, render

import articles
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    # method 가 POST 일때,
    if request.method == "POST":
        # DB에 저장하는 로직
        # field = ["title", "content"]
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            # 유효하다면 저장
            article_form.save()
            return redirect("articles:index")
    # POST 아닐때
    else:
        article_form = ArticleForm()
    # 유효하지 않을때 => 새로 작성하게끔..?
    context = {
        # 사용자 입력을 받아서 유효성 검사 종료후, 에러메시지 까지 이미 다 만들어진 article_form
        "article_form": article_form,
    }
    # context = context 차이
    return render(request, "articles/new.html", context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {"article": article}
    # detail 에서 객체 사용
    return render(request, "articles/detail.html", context)


def update(request, pk):
    # GET : From 을 제공
    article = Article.objects.get(pk=pk)
    # 저장을 위해서 분기.
    if request.method == "POST":
        # POST : 사용자로부터 값을 가져와서 검증하고, DB에 저장 인스턴스 지정 필수
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과 하면 상세보기 페이지로 이동
            article_form.save()
            return redirect("articles:detail", article.pk)
    else:
        # 위에서 생성한 객체를 넘겨준다 form에 -> 자동으로 input생성
        article_form = ArticleForm(instance=article)
    context = {
        # 기존의 존재하는 인스턴스의 값을 가지고 있는 article_form-> 기존의 값을 가지고 수정.
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)
