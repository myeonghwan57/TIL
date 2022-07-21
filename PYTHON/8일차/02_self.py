class Person:
    #사람이라면 이름이 있다.
    def __init__(self,name):
        #모든 인스턴스에 각각 name을 지정.
        self.name = name
    # self 는 인슽턴스를 내부적으로 스스로 전달해줌.
    def greeting (self):
        print(f"안녕하세요 {self.name}입니다.")

JM= Person('지민')
print(JM.name)
JM.greeting()

iu = Person('지은')
print(iu.name)
iu.greeting()