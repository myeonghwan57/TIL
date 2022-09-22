import numbers
import random
from django.shortcuts import render

# Create your views here.
def today_dinner(request):
    foods = {
            '치킨' : 'https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/5FSP3QJRCQL2JTTM2RUS7SUP2I.jpg',
            '피자' : 'https://cdn.dominos.co.kr/admin/upload/goods/20200508_KdroBehI.jpg?RS=350x350&SP=1',
            '햄버거' : 'https://images.chosun.com/resizer/zlZHiKz_wnMiQaUkoq4xB-MHx0Y=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/QWIJHKDCEBCH7JKIHE52QXW3RQ.JPG'
            }
    food = random.choice(list(foods.keys()))
    food_img = foods.get(food)
    context = {
        'food' : food,
        'food_img' : food_img,
    }
    
    return render(request,'today_dinner.html', context)
def lotto(request):
    numbers_list = []
    for _ in range(5):
        rand_num = random.sample(range(1, 45), 6)
        rand_num.sort()
        numbers_list.append(rand_num)

    context = {
        'numbers_list' : numbers_list
    }
    return render(request,'lotto.html',context)