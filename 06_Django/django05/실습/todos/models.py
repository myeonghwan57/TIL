from datetime import datetime
from django.db import models

# Create your models here. 모델정의
class Todo(models.Model):
    # pk 는 자동으로 만들어 준다.
    content = models.CharField(max_length=80)
    priority = models.IntegerField(default=3)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateField(default=datetime.now)
    # 기본속성은 데이터를 생성할때 값을 넣지 않으면 False로 자동으로 생성
    completed = models.BooleanField(default=False)
