# 모델을 통해 form CLASS를 만들수 있는 Helper
from django.db import models

# ModelForm 선언
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
