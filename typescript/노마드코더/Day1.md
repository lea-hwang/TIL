# 노마드 코더 - 타입스크립트 day 1

## 자바스크립트 대신 타입스크립트를 사용하는 이유

-> 바로 타입 안정성 때문! 



## 자바스크립트와 타입스크립트의 차이점 

### 자바스크립트

자바스크립트는 에러를 최대한 보여주지 않으려함. (실수를 피할 수 없음)

- 예시

```javascript
// 1. array와 boolean 을 합치면 문자열이 생성.. -> 에러가 발생하지 않음.
console.log([a, b, c] + false) // "a,b,cfalse"

// 2. 함수를 실행할 때, 올바른 argument를 사용하도록 강제하지 않음. 필요한 건 2개 인데, 1개만 보내도 실행됨.
function(a, b) {
  return a / b
}

divide("xxxxx") //NaN

// 3. 객체 안에 존재하지 않는 함수를 호출할 수 있음.
const nico = {name:"nico"}
nico.hello() // Uncaught TypeError
// 유저가 코드를 실행했을 때, 비로소 에러가 있다는 것을 확인할 수 있음.

```

실행했을 때 발생하는 에러, 즉 런타임 에러를 맞딱뜨리게 됨.

 -> 이러한 에러를 사전에 발견할 수 있도록 도와주는 타입스크립트를 사용.

### 타입스크립트

타입스크립트는 자바스크립트로 변환됨. 브라우저가 자바스크립트를 이해하기 때문. 자바스크립트로 변환하기 전에 실수를 확인하고 에러가 존재한다면 변환되지 않고 에러 발생.

```typescript
const nico = {
  nickname: "nick"
}

nico.hello() // 에러 발생

function divide(a, b) {
  return a / b
}
divide("hello") // 에러 발생
```



## Implicit Types vs Explicit Types

타입스크립트에서는 사용자가 데이터와 변수의 타입을 명시적으로(explicitly) 정의하거나, 아니면 사용자가 자바스크립트처럼 변수만 생성해도 된다. 작성한 코드에 따라 타입스크립트가 유추하여 변수형이 정해진다.

````typescript
//Implicit
let a = "hello" // typescript가 a라는 변수가 string 타입인걸 유추한다.
a = "bye"
a = 1 					// 자바스크립트에서는 가능하지만 타입스크립트에서는 불가능하다

//Explicit
let b : boolean = false // 명시적으로 변수 타입 설정
b = "dd" // 에러 발생

let c = [1, 2, 3]
// c가 비어있을 경우
let c : number[] = [] // 숫자를 담을 빈 배열 생성
// 타입스크립트가 변수 타입을 유추하기 어려울 때 명시적으로 작성.
c.push("1") // 에러 발생(같은 타입이 아니기 때문에)

const player = {
  name: "nico"
}
player.hello() // 에러 발생.

````

