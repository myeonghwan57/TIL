from django.urls import path
from . import views


app_name = "articles"
urlpatterns = [
    # 주문서 정의 path('주문서',views.함수 )
    # articles
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
