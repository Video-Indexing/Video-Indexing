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
function VideoItem({ video }) {
  const nav = useNavigate();
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
        <Section>duration: {video.duration}</Section>
        <ItemChapters>
          chapters:
          <br />
          {video.indexing &&
            video.tags.map((c, i) => <Chapter key={i}>{c}</Chapter>)}
        </ItemChapters>
      </VideoDescription>
    </ItemContainer>
  );
}

export default VideoItem;
