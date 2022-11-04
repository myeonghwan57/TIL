# Django ModelForm

## 개요

DB 기반의 어플리케이션 개발 과정중에서, **HTML Form(UI)** 은 **Django 모델**과 **매우 밀접한 관계**를 지닌다.

- html 에서 입력 값을 받고 넘기기 위해 form 태그를 사용한다.

- Django 모델 에 정의 했던 속성들을 그대로 html에서 사용한다.

-  model 을 바꾸거나 추가 하게 되면  html 에서 그에 맞게 form 태그를 추가 해줘야 한다.

  **=> Django 에서 제공하는 model을 기반으로 하는 form.py를 사용하면 보다 편리하게 관리 저장 사용이 가능하다.** 