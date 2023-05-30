import React from 'react';
import { Searchul, Searchli } from './SearchResults.styled';
import { FormSubTitle } from '../../utils/Form.styled';
import VideoItem from './components/VideoItem';

function SearchResultsList({ results, ignore, focusTopic }) {
  return (
    <>
      {ignore || <FormSubTitle>search results:</FormSubTitle>}
      <Searchul>
      {results && results.map((r, i) => r._id !== ignore ?? <VideoItem key={i} video={r} focusTopic={focusTopic}/>)}
      </Searchul>
    </>
  );
}

export default SearchResultsList;
