import React from "react"
import { render } from "react-dom"

import App1Container from "./containers/App1Container"

class App1 extends React.Component {
  const getData = ()=>{
    const res = fetch('http://127.0.0.1:8000/api/');
    const test = res.json();
    console.log(test);
  };
  
  render() {
    return (
      <div>
      <App1Container />
    </div>
    )
  }
}

render(<App1/>, document.getElementById('App1'))
