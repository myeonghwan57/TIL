import random
from django.shortcuts import render

# Create your views here.
def index(request):
    # 환영하는 메인페이지 보여준다.
    names = ['김명환1', '김명환2', '김명환3', '김명환4', '김명환5']
    name = random.choice(names)
    context = {
        #변수명 , 값
        'name': name,
        'img': 'https://image.shutterstock.com/image-vector/welcome-calligraphic-inscription-smooth-lines-260nw-1721907820.jpg',
    }
    return render(request,'index.html', context)


def welcome(request, name):
    # 사람들이 본인이름을 입력하면 해당이름과 환영인사를 해준다.
    context = {
        'name' : name,
        'greetings':[
            '안녕하세요', 'hello', 'Konnichiwa', 'bon jour',
        ],
        
    }
    return render(request, 'welcome.html',context)