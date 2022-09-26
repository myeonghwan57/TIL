from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def number(request, number):
    text_list = ["0", "짝수", "홀수"]
    if number == 0:
        text = text_list[0]
    elif number % 2 == 0:
        text = text_list[1]
    else:
        text = text_list[2]
    context = {
        "number": number,
        "text": text,
    }
    return render(request, "number.html", context)


def calculate(request, number01, number02):
    plus = number01 + number02
    minus = number01 - number02
    mul = number01 * number02
    divd = number01 // number02
    context = {
        "number01": number01,
        "number02": number02,
        "plus": plus,
        "minus": minus,
        "mul": mul,
        "divd": divd,
    }
    return render(request, "calculate.html", context)


def name(request):

    return render(request, "name.html")


def past_life(request):
    name = request.GET.get("name")
    king_list = ["태조", "정종", "태종", "세종", "문종", "단종", "세조", "예종", "성종"]
    king = random.choice(king_list)
    context = {
        "name": name,
        "king": king,
    }
    return render(request, "past_life.html", context)


def input(request):
    return render(request, "input.html")


def result(request):
    cnt_par = int(request.GET.get("cnt_par"))
    cnt_word = int(request.GET.get("cnt_word"))
    word_list = ["사과", "포도", "딸기", "바나나", "메론"]
    paragraph = [[] for _ in range(cnt_par)]
    for i in range(cnt_par):
        for _ in range(cnt_word):
            paragraph[i].append(random.choice(word_list))
    context = {
        "paragraph": paragraph,
    }

    return render(request, "result.html", context)
