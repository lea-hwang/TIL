# Day 3 

## call signature

```typescript
// RECAP
function add(a:number, b:number) {
    return a + b
}

// 화살표 함수
const add2 = (a:number, b:number) => a+b

// 함수의 call signature : 함수를 구현하기 이전에 input, output의 타입을 지정할 수 있음.
type Add = (a:number, b:number) => number; 

const add3: Add = (a, b) => a + b
```



## overloading

```typescript
// Overloading: 함수가 여러 개의 call signatures를 가지고 있는 것

type Add2 = {
    (a:number, b:number): number; 
    (a:number, b:string): number; 
}

const add4: Add2 = (a, b) => {
    if(typeof b === "string") return a
    return a + b

}

// Next.js 예시
type Config = {
    path:string,
    state: object
}

type Push = {
    (path:string):void
    (config:Config):void
}

const push:Push = (config) => {
    if(typeof config === "string") console.log(config)
    else {
        console.log(config.path, config.state)
    }
}

// 파라미터 개수가 다를 때
type Add3 = {
    (a:number, b:number): number
    (a:number, b:number, c:number): number
}

//변수 c가 optional
const add5:Add3 = (a, b, c?:number) => {
    if (c) return a + b + c
    return a + b
}
```

