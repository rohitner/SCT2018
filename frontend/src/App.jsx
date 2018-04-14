import React, { Component } from 'react';
import './App.css';
import Current from './components/Current';
import Login from './components/Login';
import Reddit from './components/Reddit';
import YoutubeSuggest from './components/YoutubeSuggest';
import FacebookLogin from 'react-facebook-login';

import axios from 'axios';

class App extends Component {
  constructor() {
    super();

    this.state = {
      status: "Just Started",
      curract: {mental: 'null', social: 'null'},
      loggedIn: false,
      userId: 'null',
      ytubeIds: ['JQbjS0_ZfJ0','xpVfcZ0ZcFM'],
      fbload: false
    }

    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
    this.responseFacebook = this.responseFacebook.bind(this);

  }

  responseFacebook(response) {
    console.log("Access Token:- ",response.accessToken);
    console.log("Name:- ",response.name);
    console.log(response.userID);
    console.log(response.picture.data.url);
    var fbUserData = {accessToken: response.accessToken, name: response.name, userID: response.userID, url: response.picture.data.url }
    axios.post('https://afea3443.ngrok.io/store_user', {
      accessToken: response.accessToken,
      name: response.name,
      userID: response.userID,
      url: response.picture.data.url
    })
    // .then(function (response) {
    //   axios.get()
    // })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });    
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
          <h1 className="App-title"><b>Sochack Dev</b></h1>
          <div>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        <div className='Content'>
        <div className='Youtube'><p style={{padding: '2%'}}>Here are some video suggestions you may like!</p><YoutubeSuggest ytubeIds={this.state.ytubeIds} /></div>
        <div className='Login'>
        {
          !this.state.fbload ? 
          <FacebookLogin
          appId="2011553932399327"
          autoLoad={false}
          fields="name,email,picture"
          scope="public_profile,user_friends"
          callback={this.responseFacebook} /> :
          <div></div>
        }
        
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
