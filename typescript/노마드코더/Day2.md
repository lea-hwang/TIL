# Day 2

## 타입스크립트의 타입

```typescript
// 2.2
// 명시적으로 변수 타입 정의
// number
let a : number = 1;
// string
let b : string = "i1"
// boolean
let c : boolean = true

// array
let d : number[] = [1]

// optional
// 모든 player가 name이 있지만 age는 없을 수도 있는 경우, age 뒤에 ?를 붙인다
const player : {
  name: string,
  age?: number
} = {
  name: "nico"
}
// 앞에 player.age를 작성해줘야 실행됨.
if(player.age && player.age < 10){
  
}

// Type Alias
type Name = string; // 으로 작성할 수도 있음

type Player = {
  name:string,
  age?:number
}

const nico : Player = {
  name: "nico"
}

const lynn : Player = {
  name: "lynn",
  age:12
}

// 함수의 return 타입 지정
function playerMaker(name:string) : Player {
  return {
    name
  }
}

const nico = playerMaker("nico")
nico.age = 12

// 화살표 함수
const playerMaker =  (name:string) : Player => ({name})


//2.3
type Age = number;
type Name =  string;

// readonly: property를 수정하려고 하면 에러가 발생
type Player = {
    readonly name:Name
    age?:Age
}

const playerMaker = (name:string) : Player => ({name})
const nico = playerMaker("nico")
nico.age = 12
// nico.name = "lass" // 수정하려고 했기 때문에 에러가 발생


const numbers: readonly number[] = [1, 2, 3, 4]
// numbers.push(1)  // readonly에서 는 불가능

const names: readonly string[] = ["1", "2"]
// names.push("3") // 불가능


// Tuple: array가 최소 세개의 요소를 가지고, 해당 요소의 타입을 지정하고 싶을 때, 
const player: [string, number, boolean] = ["name", 12, false]
player[0] = "hi"


//undefined & null
let a : undefined = undefined
let b : null = null


// 요소에 ?를 넣으면 undefined가 될 수 있음.
type Player2 = {
    age?:number // number이거나 undefined임.
}

// any: 비어있는 값을 쓰면 기본값이 any가 됨. Typescript로부터 빠져나오고 싶을 때 쓰는 타입. any type이 될 수 있음.
let arr = [] // any

const arr2 : any[] = [1, 2, 3, 4]
const b2: any = true
arr2 + b2 // 타입스크립트의 보호로부터 빠져나오게 됨.



//2.4
// unknown: 어떤 타입인지 모르는 변수일 때, ex) API에서 데이터를 받는데, 어떤 타입인지 모를 때.
let a:unknown;

if (typeof a === 'number') { // a가 number일 때만 실행되기 때문에 에러가 발생하지 않음.
    let b = a + 1
}

if (typeof a === 'string') { // a가 string일 때만 실행.
    let c = a.toUpperCase();
}



// void: return 값이 없는 함수, 따로 지정할 필요없이 타입스크립트가 알아서 지정해줌.
function hello() { // void
    console.log('x')
}



// never: 함수가 절대 return이 발생하지 않을때, 함수에서 예외가 발생할 때
function hello2():never {
    throw new Error("xxx")
}
// 혹은 리턴하는 타입이 두가지 이상일 때 마지막 else 부분의 절대 실행되지 않는 코드에서 name의 타입이 never가 됨
function hello3(name:string|number) {
    if (typeof name === "string") {
        name // string
    } else if (typeof name === "number"){
        name // number
    } else {
        name // never
    }
}

```

