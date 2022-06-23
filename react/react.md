## 새 프로젝트 생성

```bash
$ npx create-react-app begin-react

$ cd begin-react
$ npm start
```



## 컴포넌트 생성

### Hello.js

```javascript
import React from 'react';
// 리액트 불러오기

function Hello() {
  return <div>안녕하세요</div>
} // Hello 컴포넌트 생성

export default Hello;
// Hello 컴포넌트 내보내기
```

### App.js

```javascript
import React from 'react';
import Hello from './Hello';
// Hello 컴포넌트 불러오기

function App() {
  return (
    <div>
      <Hello />
    </div>
  );
}

export default App;
```



### index.js

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

ReactDOM.reder : 브라우저에 있는 실제 DOM 내부에 리액트 컴포넌트를 렌더링.

id가 root 인 DOM은 public/index.html에 적혀있음.



## JSX

JSX(javascript XML)는 Javascript에 XML을 추가하여 확장된 문법. HTML처럼 생겼지만 실제로는 Javascript임.

리액트 컴포넌트 파일에서 XML 형태로 코드를 작성하면 babel이 JSX를 JavaScript로 변환시켜줌.

#### Babel

자바스크립트의 문법을 확장해 주는 도구. 아직 지원되지 않는 최신 문법이나, 편의상 사용하거나 실험적인 자바스크립트 문법들을 정식 자바스크립트 형태로 변환해줌으로써 구형 브라우저같은 환경에서도 제대로 실행할 수 있게 해주는 역할을 함.



### JSX를 Javascript로 변환하기 위한 규칙

1. 닫혀있는 태그

   br과 같은 태그도 `<br />` 와 같은 형식으로 self closing 태그를 사용해야 함

2. 감싸져 있는 태그

   제일 바깥의 태그가 하나로 되어있어야 함.

   불필요한 div 태그로 감싸는게 좋지 않은 상황에서는 리액트의 `fragment`를 이용.

   ```javascript
   import React from 'react';
   import Hello from './Hello';
   
   function App() {
     return (
       <>
         <Hello />
         <div>안녕히계세요</div>
       </>
     );
   }
   
   export default App;
   ```

3. JSX 안에 자바스크립트 값 사용하기

   JSX 내부에 자바스크립트 변수를 보여줘야 할 때에는 `{}`로 감싸서 보여줌.

4. style과 className

   style과 css class를 설정하는 방법은 `background-color` 처럼 `-`로 구분되어 있는 이름을 backgroundColor 처럼 **camelCase** 형태로 작성해야함

```javascript
import React from 'react';
import Hello from './Hello';

function App() {
  const name = 'react';
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSize: 24, // 기본 단위 px
    padding: '1rem' // 다른 단위 사용 시 문자열로 설정
  }

  return (
    <>
      <Hello />
      <div style={style}>{name}</div>
    </>
  );
}
```



CSS class를 설정할 때는 `class=` 가 아닌 `className=` 으로 설정해주어야 함

```css
.gray-box {
  background: gray;
  width: 64px;
  height: 64px;
}
```

```javascript
import React from 'react';
import Hello from './Hello';
import './App.css';


function App() {
  return (
    <>
      <div className="gray-box"></div>
    </>
  );
}

export default App;
```

5. 주석

   JSX 내부의 주석은 `{/* 이런 형태로 */}` 작성함.

   열리는 태그 내부에서는 `// 이런 형태로도` 주석 작성이 가능.

   