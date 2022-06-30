# state

## Constructor 

render 함수보다 먼저 실행되면서 컴포넌트를 초기화시킬 때 필요한 코드

## state

state에 필요한 변수를 작성하고 해당 변수를 직접 사용하거나 하위 컴포넌트에 전달할 수 있음.

하위 컴포넌트에 전달할 때는 변수 = {this.state.변수명} 과 같이 작성하여 속성 형태로 태그 안에 넣어주면 된다.

## props

상위 컴포넌트에서 하위 컴포넌트로 전달한 값들은 props로 받을 수 있음. this.props.변수명으로 받아서 해당 변수를 사용할 수 있음.

## key

복수의 엘리먼트를 생성할 때는 key라는 특수한 props를 사용해야 함. 각각의 태그를 구분할 수 있도록 키로 유일한 값을 사용하는 것이 좋음.

App.js

```react
class App extends Component {
  // constructor: render 함수보다 먼저 실행되면서 컴포넌트를 초기화시킬 때 필요한 코드
  constructor(props) {
    super(props);
    this.state = {
      subject: {title:'WEB', sub:'world wide web'},
      contents: [
        {id:1, title:'HTML', desc:'HTML is for information.'},
        {id:2, title:'CSS', desc:'CSS is for design.'},
        {id:3, title:'JAVASCRIPT', desc:'Javascript if for interactive.'},
      ]
    }
  }
  render() {
    return (
      <div className="App">
        <Subject title={this.state.subject.title} subtitle={this.state.subject.sub}></Subject>
        <TOC data={this.state.contents}></TOC>
        <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    )
  }
}

export default App;

```



TOC.js

```react
import React, { Component } from 'react';

class TOC extends Component {
  render () {
    const lists = [];
    const data = this.props.data;
    let i = 0;
    while(i< data.length) {
      lists.push(<li key={data[i].id}><a href={"/content/" + data[i].id}>{data[i].title}</a></li>);
      i = i + 1;
    }
    return (
      <nav>
        <ul>
          {lists}
        </ul>
      </nav>
    )
  }
}

export default TOC;
```



