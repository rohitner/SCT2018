import React, { Component } from 'react';
import '../css/Current.css';

class Current extends Component {
    constructor() {
        super();
        this.state = {
            activity: 'Dummy variable',
        };
    }

    render() {
        return (
            <div className='Current'>
                Current Activity :- {this.state.activity}
            </div>
        )
    }
}

export default Current;