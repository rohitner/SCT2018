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
           <View>
            <View >
                <View >Current Status :- </View> <br/>
                {
                    this.state.errorflag ? <View> {this.state.status} </View> :
                    <View>
                    <View >{this.state.status.mental}</View> <br/>
                    <View >{this.state.status.social}</View>
                    </View>
                }
            </View> <br/>
            <View style={{display: 'flex'}} >
                <button style={{margin: 'auto'}} onClick={() => this.fetchHealth()}> Refresh </button>
            </View>
            </View>
        )
    }
}

export default Current;
