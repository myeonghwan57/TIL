# Python 함수 

## 1.함수 기초

**함수의 정의 ** 

- 특정한 기능을 하는 코드이 조각 모음 

- 특정명령을 수행하는 코드를 매번 작성하지 않고 필요 시간에만 호출하여 간편히 사용
  - 명령적 지식 how to 중요

- 사용자 함수 
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 정의하여 사용

**함수 사용의 이유**

- 코드 중복 방지  => 반복적인 프로그래밍을 피할 수 있다
- 재상용 용이
- 모듈화로 인한 전체적인 코드의 가독성 향상
- 문제가 발생하거나 기능의 변경이 필요할 때에도 손쉽게 유지보수 가능

## 2. 함수의 기본구조 



**선언과 호출**

- 함수 선언은def 키워드 사용
- 들여쓰기 통해 Function body(실행될 코드)  작성함 
- 함수는 parameter를 넘겨줄수 있음  
- 함수는 동작후에 return 값을 반환하면서 종료 
  - 함수는 반드시 값을 하나만 return한다
  - 함수는  return 과 동시에 실행이 종료된다



**함수의 입력** 

- parameter : 함수를 실행 할때, 함수 내부에서 사용되는 식별자
- argument : 함수를 호출 할 때 넣어주는 값.
- default Arguments Values : 기본값을 지정하여 함수 호출 시 argument 값을 설장하지 않도록 함
- positional arguments : arguments 의 위치에 따라 함수 내에 전달됨
- keyword arguments : 직졉 변수의 이름으로 특정 argument를 전달할 수 있음 
  - keyword argument 다음에  positonal argument를 활용할 수 없음

- 정해지지 않은 개수의 arguments : 여러개의  Positional Argument를 하나의 필수 parameter로 받아서 사용
  - Argument들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현
- 정해지지 않은 개수의 keyword arguments : 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정 
  - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현



**범위** 

- 함수는 내부에 local scope를 생성하며, 그 외의 공간인 global scope 로 구분
- scope
  - global scope : 코드 어디에서든 참조 할 수 있는 공간
  - local scope : 함수가 만든  scope. 함수 내부에서만 참조 가능

- variable 

  -  global variable : global scope에 정의된 변수 

  -  local variable : local scope에 정의된 변수

- 객체의 생명주기 : 각자는 수명 주기가 존재
  - built in scope : 파이썬이 실행된 이후부터 영원히 유지
  - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지 
  - local scope : 함수가 호출되고 , 함수가 종료될 때까지 유지









