# 파이썬 기초

## 기초 문법

### 변수(Variable)

> 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 변수는 할당 연산자(`=`)를 통해 값을 할당(assignment)
- `type()` : 변수에 할당된 값의 타입
- `id()` :  변수에 할당된 값(객체)의 고유한 아이덴티티(identity), 메모리주소

- 변수 할당

  > 같은 값을 동시에 할당할 수 있음

  ```python
  x = y = 1004
  ```

  > 다른 값을 동시에 할당 할 수 있음(multiple assignment)

  ```python
  x, y = 1, 2 # x, y = (1, 2)
  ```

  > 두 변수의 값 바꾸기

  ```python
  x, y = 1, 2
  # 1. 임시 변수 활용
  tmp = x
  x = y
  y = tmp
  
  # 2. pythonic
  y, x = x, y
  ```



### 식별자

> 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

- 규칙

  - 영문 알파벳, 언더스코어(`_`), 숫자로 구성

  - 처음에 숫자가 올 수 없음

  - 길이제한이 없고, 대소문자가 구별됨

  - **예약어(reserved words)**는 식별자로 사용할 수 없음

    > False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

    ```python
    import keyword
    print(keyword.kwlist)
    ```
  
  - 내장함수나 모듈 등의 이름으로도 식별자로 사용할 수 없음
  
    ```python
    print = 'hi'
    print(5)
    # TypeError: 'str' object is not callable
    # -> 이 경우 del print 하여 변수를 지워야 함.
    ```



### 입력

- `input([prompt])` 

  > 사용자로부터 값을 입력받을 수 있는 내장함수

  - 대괄호 부분에 문자열을 넣으면, 해당 문자열 출력 가능

  - 반환값은 항상 문자열(String)의 형태로 반환

  - 예시

    ``` python
    name = input('이름을 입력해주세요:')
    print(name) # type은 string
    ```



### 주석(comment)

> 코드에 대한 설명이나 다시 확인해야하는 점 등을 표시

- 한 줄 주석 : 앞에 `#`을 입력
- 여러 줄의 주석 : 한 줄씩 `#`을 사용하거나 `''' """`(docstring)으로 표현



## 파이썬 자료형(Python Datatype)

![](https://media.vlpt.us/images/jewon119/post/39e911e9-a48b-4f3c-bc54-89d9711feed1/12.jpg)

[이미지 출처](https://velog.io/@jewon119/01.-Python-%EA%B8%B0%EC%B4%88-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85data-type)



### 불린형(Boolean Type)

> True(참) 또는 False(거짓)

- 비교/논리 연산을 수행

- **0, 0.0, (), [], {}, '', None -> False ** '비어있다' 는 False

- bool() 함수

  > 특정 데이터가 참인지 거짓인지 검증



### 수치형(Numeric Type)

#### 정수(int)

> 모든 정수의 타입은 `int` (python 3 이후)

- **매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음**

  > 오버플로우(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황
  >
  > 임의 정밀도 산술(Arbitrary precision arithmetic)을 통해 가용 메모리들을 활용하여 모든 수표현에 활용

- 진수 표현

  > box로 외우자!

  - 2진수 : `0b` 
  - 8진수 : `0o`
  - 16진수 : `0x`



#### 실수(Float)

> 정수가 아닌 모든 실수

- 부동소수점

  > 실수연산 과정에서 2진수(비트)로 숫자를 표현하는 과정에서 
  >
  > floating point rounding error 발생

  - 해결방법(3번째 방법 추천)

    ```python
    # 1. 임의의 작은 수
    abs(a - b)
    
    # 2. system 상의 machine epsilon
    import sys
    print(abs(a - b) <= sys.float_info.epsilon)
    
    # 3. Python 3.5 이상 math 모듈 사용
    import math
    math.isclose(a, b)
    ```

    

#### 복소수(Complex)

> 실수부와 허수부로 구성된 복소수

- 허수부를 `j`로 표현

  ```python
  a = 3+4j
  a.real # 실수부 : 3.0
  a.imag # 허수부 : 4.0
  ```

  

### 문자열(String Type)

>모든 문자는 `str` 타입

- 문자열은 `'`나 `"`를 활용하여 표기
- **Immutable(변경불가능)**
- **Iterable(순환가능)**



#### 중첩따옴표(Nested Quotes)

> 따옴표 안에 따옴표를 표현할 경우

- 작은 따옴표가 있으면 큰 따옴표로, 큰 따옴표가 있으면 작은 따옴표로 문자열 생성



#### 삼중따옴표(Triple Quotes)

> 작은 따옴표나 큰 따옴표를 삼중`''' """`으로 사용

- 작은 따옴표, 큰 따옴표 관계없이 모두 안에 넣을 수 있음



#### Escape sequence

>문자열 내에서 특정 문자나 조작을 위해 역슬래시(`\`)를 활용

| 예약문자 | 내용(의미)        |
| -------- | ----------------- |
| \n       | 줄 바꿈           |
| \t       | 탭                |
| \r       | 케리지리턴        |
| \0       | 널(Null)          |
| \\\      | `\`               |
| \\'      | 단일인용부호(`'`) |
| \\"      | 이중인용부호(`"`) |



#### String Interpolation

> 문자열을 변수를 활용하여 만드는법

- %-formatting

  ```python
  print('Hello, 내 이름은 %s' % name)
  ```

- str.format() 

  ```python
  print("Hello, 내 이름은 {}").format(name)
  ```

- **f-strings** -> python3.6+

  ```python
  print(f"Hello, 내 이름은 {name}")
  ```



### NoneType

> '값이 없음' 표현



## 컨테이너(Container)

> 여러 개의 값을 담을 수 있는 것(객체), **서로 다른 자료형을 저장**할 수 있음

- 분류
  - 순서가 있는 데이터(Ordered)  != 정렬되어있다
  - 순서가 없는 데이터(Unordered)

![](https://media.vlpt.us/images/yeonu/post/96c0dc1d-018b-4ebc-b2c1-e6ce775059b3/2.png)

[이미지 출처](https://velog.io/@yeonu/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%90%EB%A3%8C%ED%98%95-%EA%B0%80%EB%B3%80%EA%B0%9D%EC%B2%B4-%EB%B6%88%EB%B3%80%EA%B0%9D%EC%B2%B4)



### 시퀀스형 컨테이너 (Sequence Container)

#### 리스트(List)

> 순서를 가지는 0개 이상의 객체를 참조하는 자료형

- **Mutable**(변경 가능)
- 항상 대괄호(`[]`) 형태로 출력
- 인덱스를 통해 접근 가능



#### 튜플(tuple)

> 순서를 가지는 0개 이상의 객체를 참조하는 자료형

- **Immutable**(변경 불가능)

- 항상 소괄호(`()`) 형태로 출력

- 인덱스를 통해 접근 가능

  > 생성시 주의사항
  >
  > - 단일 항목의 경우, 생성시 값 뒤에 쉼표를 붙여야 함 
  >
  >   (1,)
  >
  > - 복수 항목의 경우, 마지막 항목에는 쉼표 불필요 
  >
  >   (1,2,3)

- 튜플 대입(Tuple assignment) : 우변의 값을 좌변의 변수에 한번에 할당하는 과정

  ```python
  x, y = (1, 2)
  ```



#### 레인지(Range)

> 숫자의 시퀀스를 나타내기 위해 사용

- `range(시작, 끝, 증가량)`



------

패킹/언패킹 부터 내일