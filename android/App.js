import React from 'react';
import LinearGradient from 'react-native-linear-gradient';
import { StyleSheet, Text, View } from 'react-native';
import Current from './components/Current';
import Login from './components/Login';
export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      status: "Just Started",
      curract: {mental: 'null', social: 'null'},
      loggedIn: false,
      userId: 'null'
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
      <LinearGradient colors={['#e8cbc0' , '#636fa4']}>
      <View className="App">

      <View className="status-message">{this.state.status} </View>
      {
        this.state.loggedIn ? ( <View className='logout' ><button onClick={this.handleLogout} > Logout </button></View> )
      : (null)
      }

        <header className="App-header">
          <Text className="App-title">Sochack</Text>
          <View>Smart, Neuro-Fuzzy system based app that takes care of your mental and social health</View>
        </header>
        { !this.state.loggedIn ?
            <Login handleLogin={this.handleLogin} />
          : <Current activity={this.state.curract}  />
        }
        <View style={{'paddingTop': '2%'}} >You are in good hands :)</View>
        <View style={{'paddingTop': '26%'}}></View>
      </View>
      </LinearGradient>
    );
  }
}

const styles = StyleSheet.create({
  App: {
    textAlign: 'center',
    fontFamily: 'Titillium Web',
    /* background: linear-gradient(to bottom, indigo, white); */
    /* background: linear-gradient(to right, #355C7D, #6C5B7B, #C06C84 ); */
    // background: linear-gradient(to top, #e8cbc0 4%, #636fa4), Needed to integrate
    // We need to use extraneous function in react-native for linear gradient
    /* background: linear-gradient(to top, #283048, #859398); */
    color: 'white',
    fontSize: 130%,
  },

  // Not using
  /*App-logo : {
    animation: App-logo-spin infinite 20s linear;
    height: 80px;
  }*/

  App-header: {

    height: 150,
    padding: 20,
  },

  App-title: {
    // font-size: 1.5em;
    fontSize: 150%,
  },

  App-intro: {
    fontSize: 'large',
  },

  text: {
    textAlign: 'center',
    padding: 2%,
  },

  status-message: {
    /* display: flex; */
    position: 'fixed',
    padding: 2,
    textAlign: 'left',
    top: 2,
    left: 2,
    /* transform: translate(-50%,-50%); */

    color: '#fff',
    fontSize: 1,
    backgroundColor: '#18192b',
    borderRadius: 30,
    borderWidth: 2,
    borderStyle: solid,
    borderColor: '#3c3e63',
  },

});

export default App;
