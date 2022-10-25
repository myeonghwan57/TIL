from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 자기 자신을 참조 하는것이기 때문에 self 넣어줌
    # symmetrical = 내가 팔로우 하면 그 상대도 나를 팔로우 하게 하는 기능
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    # @property
    # def full_name(self):
    # return f'{self.last_name}{self.first_name}'
