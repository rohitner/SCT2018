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
        // this.fetchHealth = this.fetchHealth.bind(this);
    }
    componentDidMount() {
        this.fetchHealth();
        this.setState({ status: {phealth: 'Loading...', social: 'Loading...', work: 'Loading...', total: 'Loading...' } })
        console.log(this.state.status.phealth);
    }
    
    fetchHealth() {
        axios.post('http://4a436885.ngrok.io/api/health',{
            user: 'dibyadas'
        })
          .then((response) => {
          console.log(response.data.health);
          var dataGot = response.data.health;

          this.setState({ status: dataGot, errorflag: false });
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
                    <div > Social Health Status Score:-  {this.state.status.social}</div> <br/>
                    <div >Physical Health Status Score:- {this.state.status.phealth}</div> <br/>
                    <div >Work Status Score:- {this.state.status.work}</div> <br/>
                    <div >Overall Status Score:- {this.state.status.total}</div> <br/>
                    {/* <div > Social Health Status Score:-  {this.state.status.social.slice(0,5)}</div> <br/>
                    <div >Physical Health Status Score:- {this.state.status.phealth.slice(0,5)}</div> <br/>
                    <div >Work Status Score:- {this.state.status.work.slice(0,5)}</div> <br/>
                    <div >Overall Status Score:- {this.state.status.total.slice(0,5)}</div> <br/> */}
                    </div>
                } 
            </div> <br/>
            {/* <div style={{display: 'flex'}} >
                <button style={{margin: 'auto'}} onClick={() => this.fetchHealth()}> Refresh </button>
            </div> */}
            </div>
        )
    }
}

export default Current;