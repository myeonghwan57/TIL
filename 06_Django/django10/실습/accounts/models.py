from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# django.contrib.auth.models 의 AbstractUser 상속 받음
#  User 라는 클래스는 AbstractUser 상속 받음
class User(AbstractUser):
    pass
