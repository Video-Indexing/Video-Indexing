import React from 'react';
import {
  ItemChapters,
  ItemContainer,
  ItemTitle,
  VideoDescription,
  ItemP,
} from './VideoItem.styled';
function VideoItem({ video }) {
  return (
    <ItemContainer>
      <img src={video.image} height={75} />
      <VideoDescription>
        <ItemTitle>{video.title}</ItemTitle>
        <ItemChapters>
          <ItemP>chapters:</ItemP>
          {video.chapters.map((c) => (
            <p>{c}</p>
          ))}
        </ItemChapters>
        <ItemP>duration: {video.duration}</ItemP>
      </VideoDescription>
    </ItemContainer>
  );
}

export default VideoItem;
