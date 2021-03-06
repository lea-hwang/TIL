import React, { Component } from 'react';
import './App.css';
import TOC from './components/TOC'
import Content from './components/Content'
import Subject from './components/Subject'


class App extends Component {
  // constructor: render 함수보다 먼저 실행되면서 컴포넌트를 초기화시킬 때 필요한 코드
  constructor(props) {
    super(props);
    this.state = {
      mode:'welcome',
      subject: {title:'WEB', sub:'world wide web'},
      welcome:{title:'Welcome', desc:'Hello, React!!'},
      contents: [
        {id:1, title:'HTML', desc:'HTML is for information.'},
        {id:2, title:'CSS', desc:'CSS is for design.'},
        {id:3, title:'JAVASCRIPT', desc:'Javascript if for interactive.'},
      ]
    }
  }
  // state 값이 바뀌면 그 state를 가지고 있는 render 함수가 다시 호출됨. -> 화면이 다시 그려짐
  render() {
    let _title, _desc = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if (this.state.mode === 'read') {
      _title = this.state.contents[0].title;
      _desc = this.state.contents[0].desc;

    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} subtitle={this.state.subject.sub}></Subject> */}
        <header> 
          {/* 링크를 클릭했을 때 onClick에 적힌 함수가 실행됨. */}
          <h1><a href="/" onClick={function(e){
            // event.preventDefault(): 태그의 기본적인 동장을 막음
            e.preventDefault();
          }}>{this.state.subject.title}</a></h1> 
          {this.state.subject.subtitle}
        </header>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    )
  }
}

export default App;
