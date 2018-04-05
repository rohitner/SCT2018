import React, { Component } from 'react';
import './App.css';
import Current from './components/Current';

class App extends Component {
  constructor() {
    super();
    this.state = {
      status: "Just Started",
      flag: 0,
      curract: "this is new"
    };

    setInterval(() => {
      if(this.state.flag === 0){
        this.setState({
          status: "new",
          flag: 1,
          curract: "sdgdfg"
        });
      }
      else {
        this.setState({
          status: "old",
          flag: 0,
          curract: "dfnbm"
        });
      }
    },200);

  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Sochack</h1>
          <div>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        <div className="status-message"> {this.state.status} </div>
        <Current activity={this.state.curract} />
        <div className="text">
          Something is really good!
        </div>
      </div>
    );
  }
}

export default App;
