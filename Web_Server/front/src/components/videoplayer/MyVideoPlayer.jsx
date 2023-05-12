import React, { useState } from 'react';
import ReactPlayer from 'react-player'

function MyVideoPlayer() {
    return (
      <>
        {/* <div className='player-wrapper'> */}
            <ReactPlayer
            className='react-player'
            url='https://www.youtube.com/watch?v=ysz5S6PUM-U'
            width='100%'
            height='100%'
            controls = {false}
            />
        {/* </div>      */}
      </>
    );
  }
  export default MyVideoPlayer;