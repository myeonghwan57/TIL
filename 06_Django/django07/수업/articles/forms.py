from dataclasses import field
from django import forms
from .models import Article

# 나중에 css 관련 설정을 여기서 바로 설정할수 있음.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
