import React from 'react';
import {
  ItemChapters,
  ItemContainer,
  ItemTitle,
  VideoDescription,
  Section,
  Chapter,
  VideoImage,
  ImageContainer,
} from './VideoItem.styled';
import PlayButton from '../../../assets/icons/video.png';
import { useNavigate } from 'react-router-dom';

const route = 'localhost:3000/';
function VideoItem({ video, focusTopic }) {
  const nav = useNavigate();
  function hmsToSecondsOnly(str) {
    let p = str.split(':'), s = 0, m = 1;
    while (p.length > 0) {
        s += m * parseInt(p.pop(), 10);
        m *= 60;
    }
    return s;
  }
  function getDuration(indexing){
    let total = 0;
    for(const key of Object.keys(indexing)){
        const start = hmsToSecondsOnly(key.split("-")[0]);
        if(start > total)
            total = start;
    }
    return new Date(total * 1000).toISOString().slice(11, 19);
  }
  return (
    <ItemContainer
      onClick={() => window.location.replace(`playVideo/${video._id}`)}
    >
      <ImageContainer>
        <VideoImage src={video.image} height={75} className='vid-img' />
        <div className='middle'>
          <img src={PlayButton} id='play' alt='play-btn' />
        </div>
      </ImageContainer>
      <VideoDescription>
        <ItemTitle>{video.name}</ItemTitle>
        <Section>duration: {getDuration(video.indexing)}</Section>
        <ItemChapters>
          chapters:
          <br />
          {video.indexing &&
            video.tags.map((c, i) => <Chapter className={`${focusTopic===c ? "active" : ""}`} key={i}>{c}</Chapter>)}
        </ItemChapters>
      </VideoDescription>
    </ItemContainer>
  );
}

export default VideoItem;
