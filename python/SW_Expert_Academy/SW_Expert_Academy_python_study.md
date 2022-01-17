# 개념 정리

## 리스트 함수

### lambda(람다) 함수

> 함수는 간단하게 표현하는 방식, x에 매개변수를, : 다음에 식을 적음

- `lambda 매개변수 : 표현식`

- 예시

  > 10을 제곱한 값을 돌려줌

  ```python
  >>> (lambda x: x*x)(10)
  100
  ```

### map 함수

> 리스트를 일괄적으로 함수에 넣을 수 있음

- `map(함수, 리스트)`

- 예시

  > 5보다 작은 값들을 제곱함

  ```python
  >>> list(map(lambda x: x ** 2, range(5)))
  [0, 1, 4, 9, 16] 
  ```

### filter 함수

> 특정 조건에 해당하는 값들만 돌려줌

- `filter(함수, 리스트)`

- 예시

  > x가 5보다 작은 값들만 돌려줌

  ```python
  >>> list(filter(lambda x: x < 5, range(10)))
  [0, 1, 2, 3, 4]
  ```



## 아스키 코드 변환하기

### ord 함수

> 문자를 아스키 코드로 변환시켜줌

- `ord(문자)`

- 예시

  > 'a'를 아스키코드로 변환

  ```python
  >>> ord('a')
  97
  ```

### chr 함수

> 아스키 코드를 문자로 변환시켜줌

- `chr(숫자)`

- 예시

  > 65를 문자로 변환

  ```python
  >>> chr(65)
  A
  ```



## 리스트 자르기

### slicing

- `a[start: end:step]`

- 예시

  > 리스트 뒤집기

  ```python
  >>> a = 'happy'
  >>> a[::-1]
  yppah
  ```



## 함수

### 재귀함수

> 함수가 자기자신을 호출

- 예시

  > countdown

  ```python
  def countdown(n):
      if n == 0:				  # 종료조건
          print("done")
      else:
          print(n)
          return countdown(n-1) # 재귀호출
  ```

  

### 참고자료

>  [람다함수](https://wikidocs.net/64)
>
> [아스키코드 변환](https://ooyoung.tistory.com/104)