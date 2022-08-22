# python 응용,심화

## 응용, 심화

Comprehension

- list comprehension

표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

```python
[number**3 for number in range(1,4)]

# 1~3의 세제곱의 결과가 담심 리스트 
```

 

- dictonary comprehension

```python
{number : number**3 for number in range(1,4)}
#1~3의 세제곱 결과가 담긴 딕셔너리 
```

람다(lambda) 함수 

표현식을 계산한 결과값을 반환하는 함수로 이름이 없는 함수여서 익명함수라고 불림 

- 특징
  - return 문을 사용할 수 없음
  - 간편 조건문 외 조건무이나 반복문을 가질 수 없음 
- 장점
  - 함수를 정의해서 사용하는것보다 간결하게 사용가능
  - def를 사용할 숭 없는 곳에서도 사용 가능 

​	

## 파이썬 표준 라이브러리

| 명령어                      | 내용                        |
| --------------------------- | --------------------------- |
| $ pip install SomePackage   | Somepackage 설치            |
| $ pip uninstall SomePackage | Somepackage 삭제            |
| $ pip list                  | 패키지 목록                 |
| $ pip show SomePackage      | 특정 패키지 정보            |
| $ pip freeze                | 설치된 패키지의 비슷한 목록 |

