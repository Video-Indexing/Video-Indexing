import React, { useState,useRef } from 'react';
import MyVideoPlayer from '../../components/videoplayer/MyVideoPlayer';
function PlayVideo(){
    const setTopicVideosHandler = (videos) => {
        setTopicVideos(videos);    
        console.log("updated videos:",videos);
    }

    const [topicVideos, setTopicVideos] = useState([]);

    return(
        <MyVideoPlayer
            setTopicVideos ={setTopicVideosHandler}
        />
    );
}

export default PlayVideo;