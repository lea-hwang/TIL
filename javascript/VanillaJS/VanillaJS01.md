# Javascript

## 자료형

### Integer

- 1, 2, 3 .. 과 같은 정수 자료형을 의미

### Float

- 2.113, 4.322과 같은 실수 자료형을 의미

### String

- "hello" 와 같은 문자 자료형을 의미

### Boolean

- true, false와 같이 참, 거짓을 의미

### null

- 어떤 자료형에도 속하지 않은 값
- '존재하지 않는(nothing)' 값, '**비어 있는**(empty)' 값, '알 수 없는(unknown)' 값

### undefined

- 값이 **할당되지 않은** 상태를 의미

### Array

- 특정한 값들을 하나의 배열 안에 담아둔 상태를 의미

### Object

- 여러 속성을 내포하고 있는 자료형



## 변수

### 상수

- 이후에 변하지 않을 숫자(재할당 불가능)

- `const <변수명> = <값>`

```javascript
const a = 5;
const b = 7;
const myName = 'heewon'; //camel case
const isGood = true; // boolean
const hey;

console.log(a + b); // 12
console.log(hey); // undefined
```



### 변수

- 이후에 변할 가능성이 있는 숫자(재할당 가능)

- `let <변수명> = <값>`

```javascript
let money = 10000;	// integer
let names = ["John", "Leo", "Jackson", "Atom"]; // Array
let player = {
  name: "heewon",
  points: 10,
};

money = 5000;

console.log(money); // 5000
console.log(names[2]); // Jackson
```

> var이라는 변수가 있지만, 바뀌는 변수인지 아닌지 의미를 파악할 수 없게 만들어 코드의 가독성을 떨어뜨림 -> 사용하지 않음