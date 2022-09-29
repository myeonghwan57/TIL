from django import views
from django.urls import URLPattern, path

app_name = "myapp"

urlpatterns = [
    path("", views.index),
]
