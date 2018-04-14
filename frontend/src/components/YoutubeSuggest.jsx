import React, { Component } from 'react';
import { CarouselProvider, Slider, Slide, ButtonBack, ButtonNext } from 'pure-react-carousel';
import YouTube from 'react-youtube';
import '../css/react-carousel.es.css';

class YoutubeSuggest extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: this.props.ytubeIds,
            loaded: false
        }
    }

    render() {
        const opts = {
            height: '250',
            width: '300',
            playerVars: {
              autoplay: 0
            }
          };
        return (
            <CarouselProvider
            naturalSlideWidth={500}
            naturalSlideHeight={350}
            totalSlides={this.state.data.length}
            >
            <Slider>
            
            { this.state.data.map(function(arg,i,) { return <Slide index={`${i+1}`}>
            <YouTube
            videoId={arg}
            opts={opts}
            // onReady={this._onReady}
            />
            </Slide> }) }

            </Slider>
            <div className='buttons'>
            <ButtonBack className='prev' >Previous</ButtonBack>
            <ButtonNext className='next' >Next</ButtonNext></div>
            </CarouselProvider> 
        );
       
    }
    _onReady(event) {
        // access to player in all event handlers via event.target
        event.target.pauseVideo();
    }
}


export default YoutubeSuggest;