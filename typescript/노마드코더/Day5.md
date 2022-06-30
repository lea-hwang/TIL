# Day5

```typescript
// 추상 클래스: 클래스를 상속 받을 수만 있고 인스턴스를 만들지 못함.
abstract class User {
    constructor(
        private firstName: string,
        private lastName:string,
        public nickname:string
    ) {}
    //추상메소드: 추상클래스를 상속받는 모든 것을이 구현해야하는 메소드, call signiture만 가지고 있음.
    abstract getNickName(): void
    getFullName(){
        return `${this.firstName} ${this.lastName}`
    }
}

class Player extends User{
    getNickName() {
    }
}

const nico = new Player("nico", "las", "니꼬");

//nico.getFullName() private 이기 때문에 접근 불가
// private 인스턴스 밖에서 접근할 수 없고 다른 자식 클래스에서도 접근할 수 없음. 해당 클래스에서만 가능...
// protected 외부로부터는 보호되지만, 다른 자식 클래서에서 사용될 수 있음.
class Word {
    constructor(
        public englishWord: string,
        public definition: string
    ){}
}


//과제
class Dict {
    constructor(
        private words: Word[]
    ){}
    add(word:Word): void {
        this.words.push(word)
    }
    get(englishWord:string){
        for(let i = 0; i < this.words.length; i++) {
            if(this.words[i].englishWord === englishWord)  {
                return this.words[i]
            }
        }
        return null
    }
    delete(word: Word): void{
        for(let i = 0; i < this.words.length; i++) {
            if(this.words[i] === word)  {
                this.words.splice(i, 1);
                break
            }
        }
    }

    update(oldWord:Word, newWord:Word): void{
        for(let i = 0; i < this.words.length; i++) {
            if(this.words[i] === oldWord)  {
                this.words[i] = newWord
                break
            }
        }
    }
    showAll(): void{
        console.log(this.words)
    }
    count(){
        return this.words.length
    }
}
```

