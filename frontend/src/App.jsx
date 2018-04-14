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
      status: "Welcome! Please login to see your stats! :D",
      curract: {work: 'null', social: 'null', phealth: 'null', total: 'null' },
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
    // console.log(response.userID);
    // console.log(response.picture.data.url);
    // var fbUserData = {accessToken: response.accessToken, name: response.name, userID: response.userID, url: response.picture.data.url }
    // axios.post('http://0.0.0.0:5000/api/store_user', {
    //   accessToken: response.accessToken,
    //   name: response.name,
    //   userID: response.userID,
    //   url: response.picture.data.url
    // })
    // .then(function (response) {
    //   console.log(response);
    // })
    // .catch(function (error) {
    //   console.log(error);
    // });    
    this.setState({fbload: true});
  }

  handleLogin(flag, username) {
    var toset = this.state;
    return axios.post('http://0.0.0.0:5000/api/login',{ 
      user: username
    })
    .then((response) => {
      if(response.data.loginStatus == 'fail'){
        var temp = this.state.status;
        this.setState({status: 'Wrong Login'})
        setTimeout(() =>{
          this.setState({status: temp})
        },1000)
        
      }
      else{
        var temp = {mental: response.data.mental, social: response.data.social}
        this.setState({ loggedIn: true, userId: username, status: 'Welcome '+username, curract: temp});
        // console.log(toset);
        // console.log('login ka ',response);
      }
      
    });
    // this.setState(toset);
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
          <div>Smart, Fuzzy system based app that takes care of your mental and social health</div>
        </header>
        <div className='Content'>
        <div className='Youtube'><p style={{padding: '2%'}}>Here are some video suggestions you may like!</p><YoutubeSuggest ytubeIds={this.state.ytubeIds} /></div>
        <div className='Login'>
        
        { !this.state.loggedIn ? 
            (
              <div> 
              <Login handleLogin={this.handleLogin} />
              </div>
            )
          : (
              <div>
              {!this.state.fbload ?
              (<FacebookLogin
              appId="2011553932399327"
              textButton="Import friends from Facebook"
              autoLoad={false}
              fields="name,email,picture"
              scope="public_profile,user_friends"
              callback={this.responseFacebook} />) :
              <div style={{padding: '3mm'}}>You have imported your Facebook friends. You are good to go :) </div>}

              <Current activity={this.state.curract}  /> 
              </div>
            )
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
