import React, { Component } from 'react';
import './App.css';
import Current from './components/Current';
import Login from './components/Login';
import Reddit from './components/Reddit';
import YoutubeSuggest from './components/YoutubeSuggest';
// import axios from 'axios';

class App extends Component {
  constructor() {
    super();

    this.state = {
      status: "Just Started",
      curract: {mental: 'null', social: 'null'},
      loggedIn: false,
      userId: 'null',
      ytubeIds: ['JQbjS0_ZfJ0','xpVfcZ0ZcFM']
    }

    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);

  }

  handleLogin(flag, username) {
    this.setState({ loggedIn: flag, userId: username, status: 'Welcome '+username});
  }

  handleLogout() {
    this.setState({ loggedIn: false, userId: 'null', status: 'Just Started'});
  }

  render() {
    return (
      <div className="App" >

      <div className="status-message">{this.state.status} </div>
      {
        this.state.loggedIn ? ( <div className='logout' ><button onClick={this.handleLogout} > Logout </button></div> )
      : (null)
      }
      
        <header className="App-header">
          <h1 className="App-title"><b>Sochack</b></h1>
          <div>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        <div className='Content'>
        {/* <div className='Lorem'>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repellat maxime, necessitatibus perferendis odio atque voluptatum iste, earum fugiat praesentium vero libero, esse quas? Facilis fugit quod, iure dolorem harum cumque. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi qui doloribus ab nihil quasi. Necessitatibus corrupti tempore dolorum expedita natus alias facere distinctio sit quis hic, obcaecati harum quae voluptate!</div> */}
        <div className='Youtube'>Here are some video suggestions you may like!<YoutubeSuggest ytubeIds={this.state.ytubeIds} /></div>
        <div className='Login'>
        { !this.state.loggedIn ? 
            <Login handleLogin={this.handleLogin} />
          : <Current activity={this.state.curract}  /> 
        }
        </div>
        <div className='Reddit'><Reddit /></div>
      </div>
      <div style={{'paddingTop': '25%'}}></div>
      </div>
      
    );
  }
}

export default App;
