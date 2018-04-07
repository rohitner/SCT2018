import React, { Component } from 'react';
import '../css/Current.css';
import axios from 'axios';

class Current extends Component {
    constructor(props) {
        super(props);
        this.state = {
            status: this.props.activity,
            errorflag: false,
        }

        this.fetchHealth = this.fetchHealth.bind(this);
    }
    componentDidMount() {
        this.fetchHealth();
    }
    
    fetchHealth() {
        axios.get('http://0.0.0.0:5000/health')
          .then((response) => {
          console.log(response.data.health);
          this.setState({ status: response.data.health, errorflag: false });
        }).catch((error) => {
          console.log(error);
          this.setState({ errorflag: true, status: 'Error Occurred' });
        });
      }

    render() {
        return (
           <div> 
            <div >
                <div >Current Status :- </div> <br/>
                {
                    this.state.errorflag ? <div> {this.state.status} </div> :
                    <div>
                    <div >{this.state.status.mental}</div> <br/>
                    <div >{this.state.status.social}</div> 
                    </div>
                } 
            </div> <br/>
            <div style={{display: 'flex'}} >
                <button style={{margin: 'auto'}} onClick={() => this.fetchHealth()}> Refresh </button>
            </div>
            </div>
        )
    }
}

export default Current;