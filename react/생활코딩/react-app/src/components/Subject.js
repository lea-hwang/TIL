import React, { Component } from 'react';

class Subject extends Component {
  // return() 안에는 최상위 태그 하나로 감싸져 있어야 함
  render () {
    return (
      <header> 
        <h1><a href="/">{this.props.title}</a></h1> 
        {this.props.subtitle}
      </header>
    )
  }
}

export default Subject;