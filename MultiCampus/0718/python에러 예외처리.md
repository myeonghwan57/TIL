# python (에러, 예외 처리)

## 디버그/ 디버깅
`디버그(Debug)` - 버그는 말 그대로 벌레를 뜻하는 단어이며 `디버그(Debug)`는 **'벌레를 잡다.'** 라는 뜻을 가지고 있다. 
여기서 버그는 프로그램이 의도하지 않은 방향으로 실행된다거나 갑자기 오류가 발생해 실행이 중단되는 등, 프로그램의 임무를 다하지 못하는 경우를 의미한다.

`디버깅(debugging)` 또는 `디버그(debug)`는 컴퓨터 프로그램 개발 단계 중에 발생하는 시스템의 논리적인 오류나 비정상적 연산을 찾아내고 그원인을 밝혀 수정하는과정을 뜻한다.



## 에러와 예외

에러(Erorr):  

프로그램 오류 , 구문 오류 등 시스템 자체에서 비정상적인 상황이 발생한 것으로, 
 스스로 복구 및 해석이 불가능 하며 프로그램에 심각한 문제를 야기 시킬 수 있는 경우  

- 문법 에러(Syntax Error):  

  문법 에러가 발생하면, 파이썬 프로그램은 실행이 되지 않음 
  문자를 통해 파이썬이 코드를 읽어 나갈 때 문제가 발생하는 위치를 표현 
  줄에서 에러가 감지된 가장 앞의 위치를 가리키는 `캐럿(caret)기호(^)` 를 표시  

  - EOL (End Of Line)

    ```python
    print('hello
    # File "<ipython-input-6-2a5f5c6b1414>", line 1
    # print('hello
    # ^
    # SyntaxError: EOL while scanning string literal
    ```
  
  
  
  - EOL (End Of Line)
  
    ```python
    print(
    # File "<ipython-input-4-424fbb3a34c5>", line 1
    # print(
    # ^
    # SyntaxError: unexpected EOF while parsin
    ```
  
  - Inavalid syntax
  
    ```python
    while
    # File "<ipython-input-7-ae84bbebe3ce>", line 1
    # while
    # ^
    # SyntaxError: invalid synta
    ```
  
  - assign to literal
  
    ```python
    5 = 3
    # File "<ipython-input-28-9a762f2c796b>", line 
    1
    # 5 = 3
    # ^
    # SyntaxError: cannot assign to litera
    ```
  
  - TypeError
  
    ```python
    import random
    random.sample(range(3), 1, 2)
    ```
  
  - ValueError
  
    ```python
    int('3.5')
    ```
  
  - IndexError
  
    ```python
    empty_list = []
    empty_list[2]
    # ------
    # IndexError Traceback (most recent call last)
    # 1 empty_list = []
    # ----> 2 empty_list[2]
    # IndexError: list index out of rang
    ```
  
    





## 예외 처리 

try문 / except절 을 이용하여 예외 처리를 할 수 있음

try문 

- 오류가 발생할 가능성이 있는 코드를 실행 
- 예외가 발생되지 않으면 , except 없이 실행 종료

except 문 

- 예외가 방생하면 , except 절이 실행
- 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함 



작성 방법

```python
try:
    try 명령문 
except 예외그룹-1 as 변수-1 :
    예외처리 명령문 1
except 예외그룹-2 as 변수-2 :
    예외처리 명령문 2
finally : 
    finally 명령문
    
```





## 예외 발생 시키기

raise 를 통해 예외를 강제로 발생

```python
raise<표현식>(메시지) # 표현식에 예외 타입 지정 


raise
# -------
# RuntimeError Traceback (most recent call last)
# ----> 1 raise
# RuntimeError: No active exception to rerais
```

