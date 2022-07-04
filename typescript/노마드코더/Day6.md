# Day6

## 인터페이스

오브젝트의 형태를 정하기 위함.

```typescript
type Nickname = string
type Health = number
type Friends = Array<string>

type Player = {
    nickname:string,
    healthBar:number
}

const nico : Player = {
    nickname: "nico",
    healthBar: 10
}

type Food = string;

const kimchi: Food = "delcious"


type Team = "read" | "blue" | "yellow" // 3가지 중 하나만 선택해서 작성하도록 유도
type Health2 = 1 | 5 | 10

type Player2 = {
    nickname: string,
    team: Team,
    health: Health2
}

const nico2: Player2 = {
    nickname: "nico",
    team: "yellow",
    health: 10
}

// type과 동일한 방식으로 interface를 작성할 수 있음.
interface Player3 {
    nickname: string,
    team: Team,
    health: Health2
}

const nico3 : Player3 = {
    nickname: "nico",
    team: "yellow",
    health: 10
}

interface User {
    name:string
}
// interfacef를 상속
interface Player4 extends User {

}

const nico4 : Player4 = {
    name:"nico"
}

type User2 = {
    name:string
}

type Player5 = User2 & {

}

// interface는 중첩 가능
interface Person {
    name: string
}

interface Person {
    lastName: string
}

interface Person {
    health: string
}

const nico_: Person = {
    name: "nico",
    lastName: "les",
    health: "good"
}
```



## 클래스 추상화와 인터페이스 추상화의 차이점

인터페이스 

- 메소드와 property를 클래스가 가지도록 강제할 수 있다
- 자바스크립트로 컴파일 되진 않는다.
  - 추상 클래스와 비슷한 역할을 하지만 컴파일시 자바스크립트에서는 일반적인 클래스로 바뀐다.

```typescript
// 자바스크립트로 변환될 때, class로 됨
interface User2 {
    firstName:string,
    lastName:string,
    sayHi(name:string): string,
    fullName(): string
}

interface Human {
    health:number
}
// private property를 사용할 수 없음
// 여러 개의 인터페이스를 상속받을 수 있음
class Player2 implements User2, Human {
    constructor(
        public firstName:string,
        public lastName:string,
        public health:number
    ){}
    sayHi(name:string){
        return `Hello ${name}. My name is ${this.fullName}`
    }
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
}
```

