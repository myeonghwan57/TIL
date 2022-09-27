from django.urls import path
from . import views

urlpatterns = [
    # 주문서 정의 path('주문서',views.함수 )
    # articles
    path("", views.index),
    path("create/", views.create),
]
