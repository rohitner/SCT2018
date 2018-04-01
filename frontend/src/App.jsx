import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      status: "Just Started"
    };
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Sochack</h1>
          <div>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        <div className="status-message"> {this.state.status} </div>
        <div className="text">
          Something is really good!
        </div>
      </div>
    );
  }
}

export default App;
