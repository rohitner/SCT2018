import React, { Component } from 'react';
import './App.css';
import Current from './components/Current';
import Login from './components/Login';
// import axios from 'axios';

class App extends Component {
  constructor() {
    super();

    this.state = {
      status: "Just Started",
      curract: {mental: 'null', social: 'null'},
      loggedIn: false,
      userId: 'null'
    }
    this.handleLogin = this.handleLogin.bind(this);
  }

  handleLogin(flag, username) {
    this.setState({ loggedIn: flag, userId: username});
  }

  render() {
    return (
      <div className="App">

      <div className="status-message">{this.state.status} </div>

        <header className="App-header">
          <h1 className="App-title">Sochack</h1>
          <div>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        { !this.state.loggedIn ? 
            <Login handleLogin={this.handleLogin} />
          : <Current activity={this.state.curract}  /> 
        } 
        <div style={{'paddingTop': '2%'}} >You are in good hands :)</div>
        <div style={{'paddingTop': '26%'}}></div>
      </div>
    );
  }
}

export default App;
