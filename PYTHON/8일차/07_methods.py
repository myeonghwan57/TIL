# 함수 내부에서 값을 쓰고 싶을때 정의 할때 이름을 짓고, 호출할때 값을 넘겨줌 
from typing_extensions import Self


class MyClass:
    class_variable = '변수'
    def __init__(self):
        self.instance_variable
    def instance_method(self):
        return self ,self.instance_variable
    def class_method(cls):
        return cls, cls.class_variable
    def ststic_method():
        return ''
    