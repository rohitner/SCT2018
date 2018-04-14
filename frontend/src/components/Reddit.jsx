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
            var childs = response.data.data.children.splice(0,10);
           for(var i=0; i < childs.length; i++){
            //    console.log(childs[i].data.over_18);
               if((childs[i].data.over_18)){
                // console.log('removing ', childs[i]);
                childs = childs.splice(i,1);     
               }
           }
            this.setState({ data: childs,
                          loaded: true });
        
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