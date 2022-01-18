## 제어문(Control Statement)

- 위에서 아래로 순차적으로 명령 수행

## 조건문(Conditional Statement)

### 조건문 기본

> 조건식으로 참/거짓을 판단하여 상황에 따른 코드 작성

- expression에는 참/거짓에 대한 조건식

  ```python
  if < expression == True >:
      # expression이 참일 때 실행될 코드
  else:
      # expression이 거짓일 때 실행될 코드
  ```

- 예시

  > 조건문을 통해 변수 num의 홀수, 짝수 여부 출력

  ```python
  # 항상 input은 str 형태임을 잊지말자!
  num = int(input('숫자를 입력해주세요 : '))
  if num % 2: # if num % 2 == 1:
      print('홀수입니다.')
  else:
      print('짝수입니다.')
  ```

  

### 복수 조건문

>  복수의 조건식을 활용할 경우 `elif`를 활용

```python
if <expression>:
    # Code block
elif <expression>:
    # Code block
elif <expression>:
    # Code block
else: # expression이 들어갈 수 없음
    # Code block
```

- 예시

  > dust 값에 따라 미세먼지 농도에 따른 등급을 출력하는 조건식 작성

  ```python
  dust = int(input())
  # 150 초과 : 매우나쁨
  if dust > 150:
      print('매우나쁨')   
  # 80 초과 : 나쁨
  elif dust > 80:
      print('나쁨')
  # 30 초과 : 보통
  elif dust > 30:
      print('보통')
  # 나머지 : 좋음
  else:
      print('좋음')
  ```



### 중첩 조건문

> if 문을 여러개 중첩하여 작성한 조건문

```python
if <expression>:
    # Code block
    if <expression>:
        # Code block
else:
    # Code block
```



### 조건 표현식(Conditional Expression)

> 조건에 따라 값을 정할 때 활용

- 삼항 연산자(Ternary Operator)로 부르기도 함

  ```python
  <true인 경우 값> if <expression> else <false인 경우 값>
  ```

- 예시

  > value는 절대값

  ```python
  value = num if num >= 0 else -num
  ```



## 반복문(Loop Statement)

### While 문

>  조건식이 참인 경우 반복적으로 코드를 실행

```python
while <expression>:
    # Code block
```

- 예시

  > 1부터 입력한 양의 정수까지의 총합

  ```python
  user_input = int(input())
  # 값 초기화
  n = 0
  total = 0
  while n <= user_input:
      total += n
      n += 1
  print(total)
  
  # while 없이 좀 더 짧은 코드
  user_input = int(input())
  total = sum(range(1,user_input))
  print(total)
  ```

  

### For 문

>  for문은 시퀀스(string, tuple, list, range)를 포함한 **순회가능한(iterable)** 객체 요소를 모두 순회함
>
> > **Iterable** 
> >
> > - 순회할 수 있는 자료형(str, list, dict 등)
> >
> > - 순회형 함수(range, enumerate)

```python
for <변수명> in <iterable>:
    # Code block
```

- 문자열(String) 순회

  ```python
  chars = 'happy'
  # 1. 단순히 순회 (for)
  for char in chars:
      print(char)
      
  # 2. 인덱스로 접근 => 0 ~ 길이-1(반복)
  for idx in range(len(chars)):
      print(chars[idx])
  ```

- 딕셔너리(Dictionary) 순회

  ```python
  grades = {'kim' : 80, 'lee' : 100}
  # 1. 딕셔너리 순회 => key
  for key in grades:
      print(key, grades[key])
  # 2. keys
  for key in grades.keys():
      print(key, grages[key])
  # 3. values
  for value in grades.values():
      print(value)
  # 4. items
  for key, value in grades.items():
      print(key, value)
  ```

- enumerate 순회

  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환

    ```python
    >>> enumerate(iterable)
    # [(idx, iterable[idx]), ...]
    ```

  - 예시

    ```python
    chars = 'happy'
    for idx, value in enumerate(chars):
        # idx, value = (0, 'h')
        print(idx, value)
    ```

- List Comprehension

  > 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

  ```python
  [<expression> for <변수> in iterable]
  [<expression> for <변수> in iterbale if <조건식>]
  ```

  - 예시

    > 1~3의 세제곱의 결과가 담긴 리스트

    ```python
    cubic_list = []
    for number in range(1,4):
        cubic_list
    [number **3 for number in range(1,4)]
    ```

    > 1~30 숫자 중에 홀수만 출력

    ```python
    # 1. for문 
    numbers = []
    for i in range(1,31):
        if i % 2:
            numbers.append(i)
    print(numbers)
    # 2. List comprehension 사용
    numbers_2 = [i for i in range(1,31) if i % 2 == 1]
    print(numbers_2)
    ```

- Dictionary Comprehension

  > 표현식과 제어문을 통해 딕셔너리를 간결하게 생성하는 방법

  ```python
  # 기본형
  {key: value for <변수> in <iterable>}
  # 조건식이 있는 경우
  {key: value for <변수> in <iterable> if <조건식>}
  ```

  - 예시

    ```python
    # 1. for문
    cubic_dict = {}
    for i in range(1,4):
        cubic_dict[number] = number**3
    cubic_dict # {1: 1, 2: 8, 3: 27}
    
    # 2. Dictionary comprehension
    {i: i**3 for i in range(1,4)}
    ```



### 반복문 제어

- `break`

  > 반복문을 종료

  - 예시

    ```python
    for i in range(10):
        if i > 1:
            print('0과 1만 출력')
            break
        print(i)
    # 0
    # 1
    # 0과 1만 출력
    ```

- `continue`

  >  continue 이후의 코드 블록을 수행하지 않고, 다음 반복을 수행

  - `pass`와 비교

    ```python
    # pass: 해당 if문만 빠져나감
    for i in range(3):
        if i > 1:
            pass # 나중에 로직을 쓸때 사용하면 좋음
        print(i)
    # 0
    # 1
    # 2
    
    # continue: for문에서 다음으로 넘어감
    for i in range(3):
        if i > 1:
            continue
        print(i)
    # 0
    # 1
    ```

- `for-else`

  >  끝까지 반복문을 실행한 이후에 else 문 실행
  >
  > **break을 통해 중간에 종료된 경우 else문은 실행되지 않음**
  
  - 예시
  
    ```python
    for char in 'banana':
        if char == 'b':
            print('b!')
            break
    else: # break를 통해 중단되면 실행되지 않음
        print('b가 없습니다.')
    
    # 좀 더 복잡한 코드
    is_b = False
    for char in 'banana':
        if char == 'b':
            is_b = True
            break
    if is_b:
        print('b가 있습니다.')
    else:
        print('b가 없습니다.')
    ```



### for vs while

| for                        | while                                   |
| -------------------------- | --------------------------------------- |
| 반복가능한 애들을 꺼내준다 | 조건이 참일 때 실행 <br >종료조건(거짓) |

=> 결과 변수 초기화



### 유용한 사이트

[Python Tutor](https://pythontutor.com/) : 한 줄씩 실행되는 코드

