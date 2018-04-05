import React, { Component } from 'react';
import '../css/Current.css';

class Current extends Component {
    constructor() {
        super();
        // this.props = ['activity'];
        // this.state = {
        //     activity: 'Dummy variable',
        // };
        // var tempact = this.props.activity;
        // this.state = {
        //     flag: 0,
        //     activity: tempact,
        // };
        // setInterval(() => {
        //     if(this.state.flag === 0){
        //       this.setState({
        //         activity: "new",
        //         flag: 1,
        //       });
        //       this.props.activity = "sdgsd";
        //     }
        //     else {
        //       this.setState({
        //         activity: "old",
        //         flag: 0,
        //       });
        //       this.props.activity = "eryhth";
        //     }
        //   },200);
    }

    render() {
        return (
            <div className='Current'>
                Current Activity :- {this.props.activity}
            </div>
        )
    }
}

export default Current;