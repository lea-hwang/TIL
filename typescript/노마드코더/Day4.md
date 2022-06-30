# Day 4

## 다형성(Polymorphism)

poly(many) + morphos(form, structure) => many different shapes

함수가 다양한 형태를 가짐.(다양한 입력값을 받을 수 있음을 의미)

```typescript
// number, boolean, string 등 입력된 값의 타입에 따라 TypePlaceholder(generic type)를 각 타입으로 타입스크립트가 바꿔줌.
// TypePlaceholder -> generic
type SuperPrint = {
    // <TypePlaceholder>(arr: TypePlaceholder[]):void
    <TypePlaceholder>(arr: TypePlaceholder[]):TypePlaceholder
	  // <T>(arr: T[]):T

}

// const superPrint: SuperPrint= (arr) => {
//     arr.forEach(i => console.log(i))
// }

const superPrint: SuperPrint = (arr) => arr[0]

// superPrint([1, 2, 3, 4])
// superPrint([true, false, true])
// superPrint(["a", "b", "c"])
// superPrint(["a", 1, true])


const a = superPrint([1, 2, 3, 4])
const b = superPrint([true, false, true])
const c = superPrint(["a", "b", "c"])
const d = superPrint(["a", 1, true])
```

