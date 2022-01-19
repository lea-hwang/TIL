# 함수(fucntion)

> 특정한 기능을 하는 코드의 조각(묶음)

- 장점
  - 가독성
  - 재사용성
  - 유지보수

## 함수 기초

### 사용자 함수(Custom Function)

> 사용자가 직접 함수를 작성

```python
def function_name(parameter):
    # code block
    return returning_value
```



## 함수의 기본 구조

### 선언과 호출(define & call)

- `def`를 활용

- 들여쓰기를 통해 **Function body**(실행될 코드 블록)를 작성

- **parameter**를 넘겨줄 수 있음

- 동작 후 **return**된 값을 돌려 받을 수 있음

- `function_name(parameter...)`로 호출

- 예시

  > 2 + 3을 함수를 통해 구현

  ```python
  def add(x, y):
      return x + y
  add(2, 3)
  ```

  > 입력값을 세제곱 하는 함수 cube를 만들고 100의 세제곱 구하기

  ```python
  def cube(num):		# 함수 선언 및 입력값 
      return num ** 3	# 결과값
  
  cube(100)			# 함수 호출
  ```

  

### 함수의 결과값(Output)

- 결과값에 따른 함수의 종류

  - Void function

    > 명시적인 return 값이 없는 경우, `None`을 반환하고 종료

    - 예시

      ```python
      def void_add(x, y):
          print(f'{x} + {y} = {x+y}')
      ans = void_add(1, 2)
      # 1 + 2 = 3
      ans
      #
      print(ans)
      # None
      ```

  - Value returning function

    > 함수 실행 후, `return` 문을 통해 값 반환

    - `return`이 실행되었을 경우, 값 반환 후 함수가 **바로 종료**

    - 예시

      ```python
      def value_returning_add(x, y):
          return(x + y)
      value_returning_add(1, 2)
      # 3
      ans = void_add(1, 2)
      #
      ans
      # 3
      print(ans)
      # 3
      ```

    - 여러 개를 반환하고 싶을 경우, 반환값으로 **튜플** 사용

      - 예시

        > 여러 개의 출력값

        ```python
        def minus_and_product(x,y):
            return x - y, x * y
        y = minus_and_product(4, 5)
        y
        #(-1, 20)
        ```

- `return` vs `print`

  - `return` : 함수 안에서만 사용되는 **키워드**
  - `print` : 출력을 위해 사용되는 **함수**




### 함수의 입력(Input)

- Parameter

  > 함수를 실행할 때, **함수 내부**에서 사용되는 **식별자**

- Argument

  > 함수 **호출** 시 넣어주는 값

  - 소괄호 안에 할당: `func_name(argument) `

    - **필수 Argument** : 반드시 전달되어야 하는 argument

    - **선택 Argument** : 값을 전달하지 않아도 되는 argument, 기본 값이 전달

  - Positional Arguments

    > 기본적으로 Argument는 위치에 따라 함수 내에 전달

    - 예시

      ```python
      def add(x, y):
          return x + y
      
      # 위치 - 내부에서 바인딩 x = 1, y = 2
      print(add(1,2))
      ```
  
      
  
  - Keyword Arguments
  
    > 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
  
    - **Keyword Argument 다음에 Positional Argument를 활용할 수 없음**
  
    - 예시
  
      ```python
      def add(x, y):
          return x + y
      
      # 키워드 - 직접 x와 y 값을 각각 지정
      print(add(y=2, x=1))
      
      #print(add(x=1,2))
      
      # SyntaxError: positional argument follows keyword argument
      # 키워드로 지정되는 순간 위치가 이미 의미가 없어졌다 -> 에러
      print(add(1, y = 2))
      ```
  
  - Default Argument Values

    > 기본값을 지정하여 함수 호출시 argument 값을 설정하지 않도록 함

    - 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음

    - 예시

      ```python
      def add(x, y=0):
          return x + y
      add(2) 
      ```
  
  - 정해지지 않은 여러 개의 Arguments 처리
  
    - Positional Arguments **Packing/Unpacking**
  
      > `*`를 이용하여 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용
  
      - Argument들은 하나의 **tuple**로 묶임
      - 예시

      ```python
      def add(*args):
          print(args, type(args))
          
      add(1, 2, 3)
      # (1, 2, 3) <class 'tuple'>
      add(1)
      # (1,) <class 'tuple'>
      ```
  
    - keyword Argument **Packing/Unpacking**
  
      > `**`를 이용하여 Packing/Unpacking 함

      - Argument들은 **dictionary**로 묶임
      - 예시
  
      ```python
      def family(**kwagrs):
          print(kwagrs, type(kwagrs))
          
      family(father='고길동', monster='둘리')
      # 여기서 father, monster는 식별자임.
      # {'father'='고길동', 'monster'='둘리'} <class 'dict'>
      ```
  
  - 함수 정의 주의 사항
  
    - 기본 argument 값을 가지는 argument 다음에 기본 값이 없는 argument로 정의할 수 없음
  
      - 예시
  
        ```python
        def greeting(name = "lea", age):
        # SyntaxError: non-default argument follows default argument
        ```
  
    - keyword argument 다음에 positional argument를 활용할 수는 없음
  
      - 예시
  
        ```python
        add(x=3, 5)
        # SyntaxError: positional argument follows keyword argument
        ```



### 함수의 범위(Scope)

> 함수는 코드 내부에 **local scope**을 생성하며, 그 외의 공간인 **global scope**로 구분

- scope

  - global scope : 코드 **어디에서든** 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. **함수 내부**에서만 참조 가능

- variable

  - global variable : global scope에서 정의된 variable
  - local variable : local scope에서 정의된 variable

- 예시

  ```python
  def ham():
      a = 'spam'
  	
  # 1.
  # print(a) # NameError: name 'a' is not defined
  
  # 2.
  ham()
  print(a) # NameError: name 'a' is not defined
  
  # 함수는 가장 기본: local scope!
  # 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용해야 함
  # 블랙박스 밖으로 결과를 주고 싶을 때, 반드시 return 해야 함
  
  ```

- 변수 수명주기(lifecycle)

  > 변수는 각자의 수명주기(lifecycle)가 존재

  - built-in scope

    >  파이썬이 실행된 이후부터 영원히 유지

  - global scope

    > 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지

  - local scope

    > 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

- 이름 검색 규칙(Name Resolusion)

  -> NameError 와 연관

  > 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

  - `LEGB Rule`

    - `L`ocal scope: **함수**

    - `E`nclosed scope: 특정 함수의 **상위 함수**

    - `G`lobal scope: **함수 밖**의 변수, import된 **모듈**

    - `B`uilt-in scope: 파이썬 안에 **내장되어 있는 함수 또는 속성**

      > 즉, 함수 내에서는 바깥 Scope의 변수에 접근이 가능하지만 수정은 할 수 없음

    - 예시

      ```python
      a = 0
      b = 1
      def enclosed():
          a = 10
          c = 3
          def local(c):
              print(a, b, c) 
          local(300) # 10 1 300
          print(a, b, c) 
      enclosed() # 10 1 3
      print(a, b) # 0 1
      ```

- `global` 문

  > **현재 코드 블록 전체**에 적용되며, 나열된 식별자가 **global variable**임을 명시

  - 예시

    ```python
    a = 10
    def func1():
        #print(a) # error
        global a
        a = 3
        global b #이전에 선언되어 있지 않아도 됨
        b = 7
    print(a) # 10
    func1()
    print(a) # 3
    print(b) # 7 
    ```

- `nonlocal`

  > global을 제외하고 둘러 싸고 있는**(상위) scope**의 변수를 연결하도록 함

  - 예시

    ```python
    x = 0
    def func1():
        x = 1
        def func2():
            nonlocal x # 무조건 이전에 선언이 되어야 함
            x = 2
        func2() 
        print(x) 
    func1() 	# 2
    print(x) 	# 0
    ```

- 범위 확인하기

  - `globals()`

    > `global`, `local`, `built-in` 정보 모두 `dict` 형태로 정리

  - `locals()`

    > `locals()`가 실행되어지는 함수 내의 `local namespace` 들을 정리




### 함수의 문서화(Doc-String)

> 함수나 클래스의 설명
>
> `''' """`

- Naming Convention
  
  > 좋은 함수와 parameter 이름 짓는 방법
  
  - **상수** 이름은 영문 전체를 **대문자**
  - **클래스 및 예외**의 이름은 각 단어의 **첫 글자만 영문 대문자**
  - 이외 나머지는 **소문자** 또는 **밑줄**로 구분한 소문자 사용(`snake_case`)
  
  - 스스로를 설명
  
    > 이름만으로 어떤 역할을 하는 함수인지 유추 가능해야 함
  
  - 약어사용 지양



### 함수 응용

- 내장함수(Built-in Functions)

  - `map()`

    > 순회 가능한(**iterable**) 데이터구조의 모든 요소에 함수(**function**)을 적용하고, 그 결과를 **map object**로 반환

    ```python
    map(function, iterable)
    ```

    - 예시

      ```python
      n, m = map(int,input().split())
      ```

  - `filter()`

    > 순회 가능한(**iterable**) 데이터구조의 모든 요소에 함수(**function**)을 적용하고, 그 결과가 **True**인 것들을 **filter object**로 반환
    
    ```python
    filter(function, iterable)
    ```
    
    - 예시
    
      ```python
      def odd(n):
          return n % 2
      
      numbers = [1, 2, 3]
      result = filter(odd,numbers)
      
      print(result, type(result))
      # <filter obeject at ~.> <class 'filter'>
      
      list(result)
      #[1, 3]
      ```
    
      
    
  - `zip()`

    > **복수의 iterable**을 모아 **튜플**을 원소로 하는 **zip object**를 반환

    ```python
    zip(*iterables)
    ```

    - 예시

      ```python
      girls = ['jane', 'ashley']
      boys = ['justin', 'eric']
      pair = zip(girls, boys)
      print(pair, type(pair))
      # <zip objext at ~> <class 'zip'>
      
      list(pair)
      # [('jane','justin'), ('ashley', 'eric')]
      ```

  - `lambda()`

    > 표현식을 계산한 결과값을 반환하는 함수, 익명함수

    ```python
    lambda <parameter>: <expression>
    ```

    -  return 문을 가질 수 없으며 간편 조건문만 사용 가능

    - 예시

      ```python
      # 1. 람다 함수가 없을 때
      def odd(n):
          return n % 2
      
      print(list(filter(odd, range(5))))
      
      # 2. 람다 함수를 사용했을 때
      print(list(filter(lambda n: n % 2, range(5))))
      
      ```



- 재귀함수(recursive function)

  > 자기 자신을 호출하는 함수

  ```python
  def recursive_func(parameter):
      if <base case>:
          return x
      return recursive_func(argument)
  ```

  - 1개 이상의 **base case(종료되는 상황)**가 존재하고, **수렴**하도록 작성

  - 예시

    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
    factorial(4)
    ```



- 반목문과 재귀함수 비교
  - 알고리즘 자체가 재귀적인 표현이 어울릴 경우 재귀함수 사용
  - 재귀 호출은 변수 사용을 줄여줄 수 있음
  - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림



### 오늘의 +alpha

1급 객체

1. 함수의 인자로 함수 전달
2. 변수에 함수 저장
3. 리턴으로 함수 전달