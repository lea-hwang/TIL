# 파이썬 프로그래밍 기초(1) 

## 변수 

### 연습문제 1

```python
# a + aa + aaa + aaaa
a = input()
print(int(a) + int(a * 2) + int(a * 3) + int(a * 4))
```



## 연산자

### 연습문제 1

```python
a = int(input())
print(f"{a:.2f} inch =>  {a * 2.54} cm")
```



### 연습문제 2

```python
a = int(input())
print(f"{a:.2f} kg =>  {a*2.2046:.2f} lb")
```



### 연습문제 3

```python
a = int(input())
print(f"{a:.2f} ℃ =>  {a / 100 * 180 + 32:.2f} ℉")
```



### 연습문제 4

```python
a = int(input())
print(f"{a:.2f} ℉ =>  {(a - 32) / 180 * 100:.2f} ℃")
```



### 연습문제 5

```python
a = (100*0.2)/(100+200)*100
print(f"혼합된 소금물의 농도: {a:.2f}%")
```



## If

### 연습문제 1

```python
a = int(input())
for i in range(1,a + 1):
  if a % i == 0:
    print(f'{i}(은)는 {a}의 약수입니다.')
```



### 연습문제 2

```python
a = int(input())
count = 0
for i in range(1,a + 1):
  if a % i == 0:
    count = count + 1
    print(f'{i}(은)는 {a}의 약수입니다.')
  if (i == a)and (count == 2):
    print(f'{a}(은)는 1과 {a}로만 나눌 수 있는 소수입니다.')
```



### 연습문제 3

```python
a = input()
if a.isupper():
  print(f'{a} 는 대문자 입니다.')
else:
  print(f'{a} 는 소문자 입니다.')
```



### 연습문제 4

```python
Man1 = input()
Man2 = input()
if Man1 == Man2:
  print('Result : Draw')
else:
  if (Man1 == '보' and Man2 == '바위') or (Man1 == '바위' and Man2 == '가위') or (Man1 == '가위' and Man2 == '보'):
    print('Result : Man1 Win!')
  else:
    print('Result : Man2 Win!')
```



### 연습문제 5

```python
a = input()
if a.isupper(): # 대문자
  print(f'{a}(ASCII: {ord(a)}) => {a.lower()}(ASCII: {ord(a.lower())})')
else: # 소문자
  print(f'{a}(ASCII: {ord(a)}) => {a.upper()}(ASCII: {ord(a.upper())})')
```



### 연습문제 7

```python
for i in range(7,201,7):
  if i % 5 != 0:
    print(i, end = "")
  if i + 7 < 200:
    print(',', end = "")
```



### 연습문제 8

```python
for i in range(100,301,2):
  a = i//100
  b = (i%100)//10
  c = (i%10)
  if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    if i == 200:
      print(i, end = "")
    else:
      print("," + str(i), end = "")
```



## 반복 

### 연습문제 1

```python
score = [88,30,61,55,95]
for i in range(len(score)):
  if score[i] < 60:
    print(f'{i+1}번 학생은 {score[i]}점으로 불합격입니다.')
  else:
    print(f'{i+1}번 학생은 {score[i]}점으로 합격입니다.')
```



### 연습문제 2

```python
for i in range(1,101):
  print(i)
```



### 연습문제 3

```python
for i in range(2,101,2):
  if i != 100:
    print(i, end = " ")
  else:
    print(i, end = "")
```



### 연습문제 4

```python
for i in range(1,101,2):
  if i != 99:
    print(i, end = ", ")
  else:
    print(i, end = "")
```



### 연습문제 5

```python
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: ' + str(sum(range(3,100,3))))
```



### 연습문제 6

```python
BLOOD_TYPE = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
count = {'A':0,'O':0,'B':0,'AB':0}
for blood in BLOOD_TYPE:
  count[blood] = count[blood] + 1
print(count)
```



### 연습문제 7

```python
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
i = 0
while scores:
  if scores[-1] >= 80:
    sum = sum + scores[-1]
  scores.pop()
print(sum)
```



### 연습문제 8

```python
i = 5
while i > 0:
  print('*'*i)
  i = i - 1
```



### 연습문제 9

```python
i = 7
while i > 0:
  print((' ' * ((7 - i) // 2)) + ('*' * i))
  i = i - 2
```



### 연습문제 10

```python
a = input()
nums = [0 for i in range(10)]
for i in a:
  nums[int(i)] = nums[int(i)] + 1
print('0 1 2 3 4 5 6 7 8 9')
print(*nums, sep = " ")
```



### 연습문제 11

```python
for i in range(1,6):
  print(' ' * (5 - i)+ '*' * i)
```



### 연습문제 13

```python
a = int(input())
b = []
while a > 0:
  b.insert(0,a % 2)
  a = a // 2
print(*b, sep="")
```



## 함수

### 연습문제 1

```python
def flip_over(a):
  new_word = ''
  for letter in a:
    new_word = letter + new_word
  return new_word
word = input()
word2 = flip_over(word)
if word == word2:
  print(word2)
  print('입력하신 단어는 회문(Palindrome)입니다.')
```



### 연습문제 2

```python
Man1_name = input()
Man2_name = input()
Man1 = input()
Man2 = input()
if Man1 == Man2:
  print('비겼습니다!')
else:
  if (Man1 == '보' and Man2 == '바위') or (Man1 == '바위' and Man2 == '보'):
    print('보가 이겼습니다!')
  elif (Man1 == '바위' and Man2 == '가위') or (Man1 == '가위' and Man2 == '바위'):
    print('바위가 이겼습니다!')
  else:
    print('가위가 이겼습니다!')
```



### 연습문제 3

```python
a = int(input())
is_prime_num = True
for i in range(2, a):
  if a % i == 0:
    is_prime_num = False
    break
if is_prime_num:
 print('소수입니다.')
else:
 print('소수가 아닙니다.')
```



### 연습문제 4

```python
num = int(input())
fibo = [1,1]
for i in range(0,num - 2):
  fibo.append(fibo[i] + fibo[i + 1])
print(fibo)
```



### 연습문제 5

```python
old = [1, 2, 3, 4, 3, 2, 1]
new = []
for i in old:
  if not i in new:
    new.append(i)
print(old)
print(new)
```



### 연습문제 6

```python
a = [2, 4, 6, 8, 10]
print(a)
print(f'5 => {5 in a}')
print(f'10 => {10 in a}')
```



### 연습문제 7

```python
a = int(input())
factorial = 1
for i in range(1, a + 1):
  factorial = factorial * i
print(factorial)
```



### 연습문제 8

```python
a = list(map(int, input().split(',')))
for num in a:
  print(f'square({num}) => {num ** 2}')
```



### 연습문제 9

```python
a = input().split(', ')
if len(a[0])>len(a[1]):
  print(a[0])
else:
  print(a[1])
```



### 연습문제 10

```python
def countdown(a):
  if a <= 0:
    print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
  else:
    for i in range(10,0,-1):
      print(i)
countdown(0)
countdown(10)
```



## 내장함수 

### 연습문제 1

```python
name = input()
age = int(input())
year = 2019 - age + 100
print(f'{name}(은)는 {year}년에 100세가 될 것입니다.')
```



### 연습문제 4

```python
line = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")
k = list(map(lambda x: 4 if x == "A" else 3 if x == "B" else 2 if x == "C" else 1, line))
print(sum(k))

### 다른 방식 ## 
line = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")
k = list(map(lambda x: ord('E') - ord(x), line))
print(sum(k))
```



### 연습문제 5

```python
a = [1, 2, '4', 3]
for i in a:
  if str(type(i)) != "<class 'int'>":
    print("에러발생")
```



### 연습문제 6

```python
a = input()
print(f'ASCII {a} => {chr(int(a))}')
```



### 연습문제 7

```python
print(list(filter(lambda x: x % 2 == 0, range(1,11))))
```



### 연습문제 8

```python
print(list(map(lambda x: x*x,range(1,11))))
```



### 연습문제 9

```python
a = list(filter(lambda x:x % 2 == 0, range(1,11)))
print(list(map(lambda x: x*x,a)))
```



### 연습문제 10

```python
a = [3, 5, 4, 1, 8, 10, 2]
print(f'max(3, 5, 4, 1, 8, 10, 2) => {max(a)}')
```



### 연습문제 11

```python
dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
for i in dic.keys():
  print(f"{i}: {dic[i]}")
```