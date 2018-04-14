import React, { Component } from 'react';
import '../css/Login.css';
// import axios from 'axios';

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {username: '', password: ''};
        
        this.handleUserChange = this.handleUserChange.bind(this);
        this.handlePassChange = this.handlePassChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleUserChange(event) {
        this.setState({username : event.target.value});
    }

    handlePassChange(event) {
        this.setState({password : event.target.value});
    }

    handleSubmit(event) {  
        this.props.handleLogin(true,this.state.username);
    }

    render() {
        return(
            <div className='form-input'>
            <label htmlFor="form-input"> Login </label> <br/> <br/>
            
            <input type='text' value={this.state.username} placeholder='Username' onChange={this.handleUserChange} /> <br/> <br/>

            <input type='password' value={this.state.password} placeholder='Password' onChange={this.handlePassChange} /> <br/> <br/> 

            <input type='button' value='Login' onClick={this.handleSubmit} />

            </div>
        )

    }
}

export default Login;