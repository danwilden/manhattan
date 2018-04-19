import React from "react"

import Headline from "../components/Headline"

export default class App1Container extends React.Component {
  const getData = ()=>{
    const res = fetch('http://127.0.0.1:8000/api/');
    const test = res.json();
    console.log(test);
  };
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>I can't seem to get it to work</Headline>
            <button onClick=getData()>Click Me</button>
          </div>
        </div>
      </div>
    )
  }
}
