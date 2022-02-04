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

- **인스턴스 변수**

  - **인스턴스가 개인적으로 가지고 있는 속성(attribute)**
  - 각 인스턴스들의 고유한 변수
  - 생성자 메소드에서 **`self.<name>`으로 정의**
  - 인스턴스가 생성된 이후 **`<instance>.<name>`으로 접근 및 할당**

- **인스턴스 메소드**

  - **인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정**하는 메소드

  - 클래스 내부에 정의되는 메소드의 기본

  - 호출 시, **첫번째 인자로 인스턴스 자기자신(`self`)이 전달됨**

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

- **생성자(constructor) 메소드**
  
  - 인스턴스 객체가 **생성**될 때 자동으로 호출되는 메소드
  - 인스턴스 **변수들의 초깃값**을 설정
    - 인스턴스 생성
    - `__init__` 메소드 자동 호출 
  
- **소멸자(destuctor) 메소드**

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

- **매직 메소드**

  - Double underscore(`__` 던더)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 스페셜 메소드 혹은 매직 메소드라고 불림

  - 특정 상황에 자동으로 불리는 메소드

  - 객체의 특수 조작 행위를 지정(함수, 연산자 등)

  - 다른 인스턴스를 가리킬 때, `other`를 사용

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

- **클래스 변수**

  > 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 속성(`attribute`)

    > 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 선언 내부에서 정의

  - **`<classname>.<name>`으로 접근 및 할당**

  - 한 번 변경하면 다른 모든 인스턴스에도 영향

  - `<instance>.<클래스 변수명>`으로 접근이 가능하긴 함.

  - **`<instance>.<클래스 변수명>`으로 값을 새로 할당할 경우 해당 변수는 인스턴스 변수로 새롭게 생성됨. 다른 인스턴스에는 클래스 변수가 남아있음(클래스 변수가 사라지진 않음)**

    ``` python
    class Circle:
        pi = 3.14
        def __init__(self, r):
            	self.r = r
        def area(self):
            return self.pi * r ** 2
    print(Circle.pi)
    ```
    
    

- **클래스 메소드**

  > 클래스가 사용할 메소드

  - `@classmethod` 데코레이터를 사용하여 정의

    - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

  - 호출 시, **첫번째 인자로 클래스(`cls`)가 전달됨**

    ```python
    class MyClass:
        var = 'Class 변수'
        
        @classmethod
        def class_method(cls):
            print(cls.var)
            return cls
    ```



- **스태틱 메소드**

  > 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

  - 클래스가 사용할 메소드

  - `@staticmethod` 데코레이터를 사용하여 정의

  - 호출 시, **어떠한 인자도 전달되지 않음**(클래스 정보에 접근/ 수정 불가)

  - 상속시 메소드 상속됨

    ```python
    class MyClass:
        @staticmethod
        def class_method(arg1, ...):
            pass
    MyClass.static_method(..)
    ```




- 인스턴스와 클래스 간의 이름공간(`namespace`)
  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

|                 | 호출방법                              | 특징                                                         |
| --------------- | ------------------------------------- | ------------------------------------------------------------ |
| 인스턴스 메소드 | 인스턴스.메서드() <br>인스턴스가 호출 | def method(self)<br>self: 호출 인스턴스 정보                 |
| 클래스 메소드   | 클래스.메서드()<br> 클래스가 호출     | @classmethod<br>def method(cls)<br>cls: 호출한 클래스 정보   |
| 스태틱 메소드   | 클래스.메서드()<br>클래스가 호출      | @staticmethod<br>def method()<br>어떤 정보도 자동 전달되는게 없다 |

**인스턴스에서는 클래스 메서드, 스태틱 메서드에 접근가능(호출가능) 이지만, 굳이 그렇게 하지 않음.**

스태틱메소드는 클래스나 인스턴스에 접근할 수 없음.

## 메소드

- 인스턴스 메소드
  - `self` 매개변수를 통해 동일한 객체에 정의된 속성 및 다른 메소드에 자유롭게 접근 가능
  - 클래스 자체에도 접근 가능 -> **인스턴스 메소드가 클래스 상태를 수정할 수도 있음**
- 클래스 메소드
  - 클래스를 가리키는 `cls` 매개 변수를 받음
  - `cls` 인자에만 접근할 수 있기 때문에 **객체 인스턴스 상태를 수정할 수 없음**
- 스태틱 메소드
  - 임의개수의 매개변수를 받을 수 있지만, `cls`,`self`나 매개변수는 사용하지 않음
  - **객체 상태나 클래스 상태를 수정할 수 없음**
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스로 한정하는 용도로 사용





# 객체지향의 핵심개념

## 추상화

> 데이터나 프로세스를 의미, 수행과정이 비슷한 개념으로 묶어 정의(선언) 하는 것

- dog, cat -> pet으로 묶기(추상화)



## 상속

> 두 클래스 사이 부모 - 자식 관계를 정립하는 것

- 클래스는 상속이 가능함

  - 모든 파이썬 클래스는 object를 상속 받음

  ```python
  class ParentClass:
      pass
  class ChildClass(ParentClass):
      pass
  ```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음

- 부모클래스의 속성, 메스드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def talk(self):
          print(f'반갑습니다. {self.name}입니다.')
  
  class Professor(Person):
      def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
          
  class Student(Person):
      def __init__(self, name, age, gpa):
          self.name = name
          self.age = age
          self.gpa = gpa
      def talk(self):
          print(f'안녕하세요.{self.name}입니다')
  p1 = Person('heewon', 30)
  p1.talk()
  
  p2 = Professor('j', 50, '컴공')
  p2.talk()
  
  p3 = Student('dd', 20, 4.5)
  p3. talk()
  ```



- `isinstance(object, classinfo)`

  > classinfo의 instance거나 subclass*인 경우 True

- `issubclass(class, classinfo)`

  > class가 classinfo의 subcalss면 True
  >
  > classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사

  ```python
  print(isinstance(p1, Person)) #True
  print(isinstance(p1, Student)) #False
  int() # -> class임
  type(3) # -> <class 'int'>
  # bool은 int의 하위 클래스
  # int float은 별개의 클래스
  ```



- `super()`

  > 자식클래스에서 부모클래스를 사용하고 싶은 경우

  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def talk(self):
          print(f'반갑습니다. {self.name}입니다.')
  
  class Professor(Person):
      def __init__(self, name, age, department):
          super().__init__(name, age)
          self.department = department
          
  pp1 = Professor('bob', 55, '경영')
  pp1.name
  ```



- 다중 상속

  - 두개 이상의 클래스를 상속받는 경우
  - 상속 받은 모든 클래스의 요소를 활용 가능함
  - 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

  ```python
  class Mom:
      gene = 'XX'
  class Dad:
      gene = 'XY'
  class Baby(Mom, Dad): # Mom이 먼저 상속됨
      pass
  baby = Baby()
  baby.gene # XX
  ```

  

- `mro` 메서드 (Method Resolution Order)

  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드
  - **기존의 인스턴스 -> 클래**스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 **인스턴스 -> 자식 클래스 -> 부모 클래스**로 확장

  

## 다형성

> 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

- 메소드 오버라이딩

  > 상속 받은 메소드를 재정의

  - 클래스 상속 시, 부모 클래스에서 정의한 메소드를 **자식 클래스에서 변경**
  - 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
  - 상속받은 메소드를 재정의
    - 상속받은 클래스에서 같은 이름의 메소드로 덮어씀
    - 부모 클래스의 메소드를 실행시키고 싶을 경우 super를 활용



## 캡슐화

> 객체의 일부 구현 내용에 대한 외부로부터 직접적인 액세스를 차단
>
> 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

- 접근제어자

  - Public Access Modifier

    > 어디서나 호출 가능함

    - 언더바가 없이 시작하는 메소드나 속성
    - 하위 클래스 `override` 허용
    - 일반적으로 작성되는 메소드와 속성의 대다수를 차지

  - Protected Access Modifier

    > **암묵적 규칙**에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능

    - 언더바 1개(`_`)로 시작하는 메소드나 속성
    - 하위 클래스 `override` 허용

  - Private Access Modifier

    > 본 클래스 내부에서만 사용이 가능

    - 언더바 2개(`__`)로 시작하는 메소드나 속성
    - 하위클래스 상속 및 호출 불가능 (**오류**)
    - 외부 호출 불가능(**오류**)

- getter 메소드와 setter 메소드

  - 변수에 접근할 수 있는 메소드를 별도로 생성
  - getter 메소드 : 변수의 값을 읽는 메소드
    - `@property` 데코레이터 사용
  - setter 메소드: 변수의 값을 설정하는 성격의 메소드
    - 메소드를 속성으로 변경한다고 생각하면 됨
    - `@변수.setter` 사용

  ```python
  def Person:
      def __init__(self, name, age):
          self.name = name
          self._age = age
      
      @property
      def age(self):
          return self._age
      
      @age.setter
      def age(self):
          self._age = self._age - 10
  
  p1 = Person(20)
  print(p1.age) # 20
  
  p1.age = 33
  print(p1.age) # 23
  ```

  

​	