# 에러 예외처리

## 디버깅

- branches: 모든 조건이 원하는 대로 동작하는지
  - 이상, 이하, 초과, 미만 끝 값
- for loops: 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops: 종료 조건
- function: 호출, 파라미터, 결과, 타입
- 

## 에러와 예외

- 문법 에러(Syntax Error)

  > SyntaxError 가 발생하면, 파이썬 프로그램은 **실행되지 않음**

  - invalid syntax
  - assign to literal
  - EOL (End of Line)
  - EOF (End of file)

- 예외(Exception)

  > 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 **실행을 멈춤**

  - ZeroDivisionError : 0을 나누고자 할 때 발생
  - NameError: namespace 상에 이름이 없는 경우(이름의 오타)
  - TypeError: 타입 불일치
    - 타입이 다른 것 끼리 연산
    - 함수 인자 타입
    - argument 누락
    - argument 개수 초과
    - argument type 불일치
  - ValueError: 타입은 올바르나 값이 적절하지 않거나 없는 경우
  - IndexError: 인덱스가 존재하지 않고나 범위를 벗어나는 경우
  - KeyError: 해당 키가 존재하지 않는 경우
  - ModuleNotFoundError: 존재하지 않는 모듈을 import 하는 경우
  - ImportError: Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우
  - KeyboardInterrupt: 임의로 프로그램이 종료되었을 때
  - IndentationError: Indentation이 적절하지 않는 경우
  - 

## 예외 처리

- try 문(statement) except

  ```python
  try:
      pass
  except:
      pass
  finally:
      pass
  ```

  

## 예외 발생 시키기

