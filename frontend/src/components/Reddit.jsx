import React, { Component } from 'react';
import RedditItem from './RedditItem';
import { CarouselProvider, Slider, Slide, ButtonBack, ButtonNext } from 'pure-react-carousel';
import '../css/Reddit.css';
import '../css/react-carousel.es.css';
import axios from 'axios';

class Reddit extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: '',
            loaded: false
        }

        this.fetchNews = this.fetchNews.bind(this);
    }
    componentDidMount() {
        this.fetchNews();
    }
    
    fetchNews() {
        axios.get('https://www.reddit.com/r/UpliftingNews/top/.json?count=10')
          .then((response) => {
          this.setState({ data: response.data.data.children.splice(0,10),
                          loaded: true });
          console.log("reddit ",this.state.data)
        }).catch((error) => {
          console.log(error);
        //   this.setState({ errorflag: true, status: 'Error Occurred' });
        });
      }

    render() {
        return (
           <div>
               <p>Some uplifting news we think you would like :D</p>
               {  
                this.state.loaded ?
                <CarouselProvider
                naturalSlideWidth={100}
                naturalSlideHeight={125}
                totalSlides={this.state.data.length}
                >
                <Slider>
                { this.state.data.map(function(arg,i) { return <Slide index={`${i+1}`}><RedditItem data={arg.data} /></Slide> }) }
                
                </Slider>
                <div className='buttons'>
                <ButtonBack className='prev' >Previous</ButtonBack>
                <ButtonNext className='next' >Next</ButtonNext></div>
                </CarouselProvider> :
                <div></div>
               }
            
           </div>
        )
    }
}


export default Reddit;