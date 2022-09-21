# python

## 1.computer programming language

- 컴퓨터 : calculation + remember  => 계산하다. + 기억한다(메모리).

- 프로그래밍 : 명령어의 모음(집합)

- 언어 : 자신의 생각을 나타내고 전달하기 위해 사용하는 체계 

=> computer programming language => 컴퓨터에게 명령하는 말 (정의) / 컴퓨터에게 명령하기 위한 약속 



​	선언적 지식 (declarative - knowledge) - "사실에 대한 내용"

​	명령적 지식 (imperative - knowledge) - "How-to" 



## 2. 파이썬이란?

- Easy to learn
  - 다른 프로그래밍 언어보다 문법이 간단하면서도 어렵지 않음 
  - 문법이 매우 간결 -> 짧은 시간에 배울수 있음.

- Expressive language

  - 같은 작업이라도 다른 언어들에 비해 매우 간결함.

    ```java
    public class HelloPython{
        public static void main (Stirng[] args){
            System.out.println("Hello Python!");
        }
    }
    ```

    ```python
    print("hello python!")
    ```

    

- Cross flatform language

  - 다양한 운영체제에서 실행 가능.

- 인터 프리터 언어 (Interpreter)

  - 소스코드를 기계와 얘기 하듯이 한줄 입력한 후 바로 확인 가능.

- 객체 지향 프로그래밍(Object Oriented Programming)

  - 모든것이 객체로 구현되어 있음.

    

## 3.기초문법

- 코드 스타일 가이드에 따라서 코드 작성 
  - 파이썬에서 제안하는 스타일 가이드가 존재함.
  - PEP8 (https://www.python.org/dev/peps/pep-0008/ ) 

- **변수** : 메모리 어딘가에 저장되어 있는객체를 참도하기 위해 사용되는 이름 

  - 동일 변수 이름에 언제든지 다른 객체를 할당할수 있다. (상자)

  - 할당 연산자`=`를 통해 값을 할당(assignment)

    ``` python
    x = 5
    y = 3
    s = 'python'
    a = b = 4 #값을 동시에 할당 할 수 있음.
    a, b = 1, 2 # 다른값을 동시에 할당 할 수 있음.
    ```

    - 식별자를 사용해서 할당을 하면 안됨. (식별자 : 키워드/ 예약어/ 내장함수/ 모듈 )

      => 기존의 이름에 다른값을 할당하게 되므로 더이상 동작하지 않음.

- **주석** : 코드에 대한 설명 => 가장 중요한 점이나 다시 확인해야 하는 부분 표시 

  - 컴퓨터는 인식하지 않음 `#`을 사용해 한줄 주석을 만들 수 있다.

    ``` python
    # 주석은 #을 사용해서 작성한다.
    # print('Hello')
    ```

    



