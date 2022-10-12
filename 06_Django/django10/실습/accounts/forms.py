from django.contrib.auth.forms import UserCreationForm

# from .models import User -> models.py 에 있는 User 직접참조하지 않는다
# auth.User 가 기본 커스텀해서 사용하는걸 권장.
#
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
