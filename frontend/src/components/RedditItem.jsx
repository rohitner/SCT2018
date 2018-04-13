import React, { Component } from 'react';
import '../css/RedditItem.css';
// import axios from 'axios';

class RedditItem extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: this.props.data,
        }
    }

    componentDidMount(){
        console.log(this.state.data);
    }

    render() {
        var date = new Date(1000 * this.state.data.created);
        return (
            <div className='cardcon' > 
            <div className="example-2 card">
            <div className="wrapper">
              <div className="header">
                <div className="date">
                  <span className="day">{date.getDate()}/</span>
                  <span className="month">{date.getMonth() + 1}/</span>
                  <span className="year">{date.getFullYear()}</span>
                </div>
              </div>
              <div className="data">
                <div className="content">
                  <span className="author">Posted by /u/{this.state.data.author}</span>
                  <h1 className="title"><a target='_blank' href={this.state.data.url}>{this.state.data.title}</a></h1>
                  <p className="text">For more such news, visit Reddit's Uplifiting News</p>
                </div>
              </div>
            </div>
          </div>
          </div>
        )
    }
}

export default RedditItem;