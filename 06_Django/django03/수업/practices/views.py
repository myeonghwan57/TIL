
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)
    # request, html 파일 이름, context

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(request)
    # print(request.GET.get('ball'))
    # ball = request.GET.get('ball')
    # context = {
    #     'name' : ball, #템플릿 안에서 사용할 것 : 데이터
    # }
    
    return render(request, 'pong.html',{'name' : request.GET.get('ball')})
