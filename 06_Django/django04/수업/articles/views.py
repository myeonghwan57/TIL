from django.shortcuts import render
from .models import Article

guest_book = []


# Create your views here.
def index(request):
    guest_book = Article.objects.all()
    return render(request, "articles/index.html", {"guest_book": guest_book})


def create(request):
    content = request.GET.get("content")
    # guest_book.append(content)
    # db에 저장
    Article.objects.create(content=content)
    return render(request, "articles/create.html", {"content": content})
