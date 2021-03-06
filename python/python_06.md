# 에러 예외처리

## 디버깅

> 디버깅 시 생각해야 할 요소들은 다음과 같다.

- branches: 모든 조건이 원하는 대로 동작하는지
  - 이상, 이하, 초과, 미만 끝 값

- for loops: 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops: 종료 조건
- function: 호출, 파라미터, 결과, 타입

## 에러와 예외

- 문법 에러(**Syntax Error**)

  > SyntaxError가 발생하면, 파이썬 프로그램은 **실행되지 않음**
  >
  > 캐럿(caret)기호(`^`)를 통해 파이썬이 코드를 읽어 나갈 때(**parser**) 문제가 발생한 위치를 표현

  - invalid syntax : 문법상 오류
  - assign to literal : literal에 할당하려고 시도했을 때 뜨는 에러
  - EOL (End of Line):  문자열을 스캐닝할 때 에러 발생
  - EOF (End of file): 갑자기 파일의 끝이 올 것을 예상치 못함(즉 닫히지 않은 함수나 문법 상의 에러가 있다는 뜻)

- 예외(**Exception**)

  > 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 **실행을 멈춤**

  - ZeroDivisionError : 0을 나누고자 할 때 발생
  - NameError: namespace 상에 이름이 없는 경우, 주로 이름의 오타
  - TypeError
    - 타입 불일치
    - argument 누락
    - argument 개수 초과
    - argument type 불일치
  - ValueError: 타입은 올바르나 값이 적절하지 않거나 없는 경우
  - IndexError: 인덱스가 존재하지 않거나 범위를 벗어나는 경우
  - KeyError: 해당 키가 존재하지 않는 경우
  - ModuleNotFoundError: 존재하지 않는 모듈을 import 하는 경우
  - ImportError: Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우
  - KeyboardInterrupt: 임의로 프로그램이 종료되었을 때
  - IndentationError: Indentation이 적절하지 않는 경우

## 예외 처리

- try 문 (statement) / except 절 (clause)을 이용하여 예외 처리를 할 수 있음

- `try` 문

  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
  
- `except` 문

  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

  ```python
  try:
      try 명령문
  except 예외그룹-1 as 변수-1 :
      예외처리 명령문 1
  except 예외그룹-2 as 변수-2 :
      예외처리 명령문 2
  finally: #선택사항
      finally명령문
  ```

  

## 예외 발생 시키기

