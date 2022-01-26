# 객체지향 프로그래밍(OOP)

>파이썬은 모두 **객체(object)**로 이루어져 있다.

### 객체(object)

>객체(object)는 특정 타입의 **인스턴스(instance)** 이다.

- 123, 900, 5는 int의 인스턴스

- 'hello'는 string의 인스턴스

- [123, 12, 21]는 list의 인스턴스

- 객체(object)의 특징

  > **객체(object)** = **속성(Attribute)** + **기능(Method)**

  - 타입(type): 어떤 연산자(oprator)와 조작(method)가 가능한가?
  - 속성(attribute): 어떤 상태(데이터)를 가지는가?
  - 조작(method): 어떤 행위(함수)를 할 수 있는가?

### 객체지향 프로그래밍

> 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍

- VS. 절차지향 프로그래밍
  - 객체지향: 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)
  - 절차지향: 데이터와 함수로 인한 변화

- 필요한 이유
  - 현실 세계를 프로그램 설계에 반영(추상화)
- 장점
  - 프로그램을 유연하고 변경이 용이하게 만듦
  - 소프트웨어 개발과 보수를 간편하게 함



## OOP 기초

- 기본 문법

  - 클래스 정의

    ```python
    class MyClass:
        pass
    ```

  - 인스턴스 생성

    ```python
    my_instance = MyClass()
    ```

  - 메소드 호출

    ```python
    my_instance.my_method()
    ```

  - 속성

    ```python
    my_instance.my_attribute
    ```

- 클래스와 인스턴스

  > 객체의 틀(클래스)을 가지고 객체(인스턴스)를 생성한다.
  >
  > - 클래스 : 객체들의 분류(class)
  >
  > - 인스턴스 : 하나하나의 실체/예(instance)

- 속성(attribute)

  > 특정 데이터 타입/클래스의 객체들이 가지게 될 **상태/데이터를 의미**

- 메소드(method)

  > 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(**함수**)

- 객체 비교

  - `==`

    > 동등한(equal)
    >
    > 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    >
    > 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해준 것은 아님

  - `is`

    > 동일한(identical)
    >
    > 두 변수가 동일한 객체를 가리키는 경우 True



## 인스턴스

- 인스턴스 변수

  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수
  - 생성자 메소드에서 `self.<name>`으로 정의
  - 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

- 인스턴스 메소드

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드

  - 클래스 내부에 정의되는 메소드의 기본

  - 호출 시, 첫번째 인자로 인스턴스 자기자신(`self`)이 전달됨

    ```python
    class MyClass:
        def instance_method(self, arg1, ...):
            pass
    my_instance = MyClass()
    my_instance.instance_method(...)
    ```

- `self`

  - **인스턴스 자기자신**
  - 파이썬에서 인스턴스 메소드는 호출 시 **첫번째 인자**로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 `self`를 첫번째 인자로 정의
    - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자(constructor) 메소드
  - 인스턴스 객체가 **생성**될 때 자동으로 호출되는 메소드
  - 인스턴스 **변수들의 초깃값**을 설정
    - 인스턴스 생성
    - `__init__` 메소드 자동 호출 

- 소멸자(destuctor) 메소드

  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드
  - `__del__` 메소드 자동 호출

  ```python
  class Person:
      def __init__(self): # constructor
          # 인스턴스 변수를 정의하기 위해 사용!
          print('인스턴스가 생성되었습니다.')
      def __del__(self): # destructor
          print('인스턴스가 삭제되었습니다.')
  p1 = Person()
  del p1
  ```

- 매직 메소드

  - Double underscore(__)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 스페셜 메소드 혹은 매직 메소드라고 불림

  - 특정 상황에 자동으로 불리는 메소드

  - 객체의 특수 조작 행위를 지정(함수, 연산자 등)

  - 예시

    - `__str__(self)`, `__len__(self)`, ...

    ```python
    class Person:
        def __init__(self, name, age, height):
            self.name = name
            self.age = age
            self.height = height
        def __gt__(self, other): # greater than
            return self.age > other.age
        def __len__(self):
            return self.height
        def __str__(self):
            return f'{self.name} : {self.age}살'
    p1 = Person('희원', 111, 190)
    p2 = Person('지은', 10, 185)
    p1 > p2 # -> 111>10 ->True
    len(p1) # -> 190
    print(p1) # 희원 : 111살
    ```

    

## 클래스

- 클래스 변수

  > 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 속성(`attribute`)

    > 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 선언 내부에서 정의

  - `<classname>.<name>`으로 접근 및 할당

  - 한 번 변경하면 다른 모든 인스턴스에도 영향

    ``` python
    class Circle:
        pi = 3.14
        def __init__(self, r):
            	self.r = r
        def area(self):
            return self.pi * r ** 2
    ```

    

- 클래스 메소드

  > 클래스가 사용할 메소드

  - `@classmethod` 데코레이터를 사용하여 정의

    - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

  - 호출 시, 첫번째 인자로 클래스(`cls`)가 전달됨

    ```python
    class MyClass:
        var = 'Class 변수'
        
        @classmethod
        def class_method(cls):
            print(cls.var)
            return cls
    ```

- 스태틱 메소드

  > 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

  - 클래스가 사용할 메소드

  - `@staticmethod` 데코레이터를 사용하여 정의

  - 호출 시, **어떠한 인자도 전달되지 않음**(클래스 정보에 접근/ 수정 불가)

    ```python
    class MyClass:
        @staticmethod
        def class_method(arg1, ...):
            pass
    MyClass.static_method(..)
    ```

    

## 메소드

> ㅇ





# 객체지향의 핵심개념

## 추상화

> 

## 상속

> 

## 다형성

> 

## 캡슐화

> 