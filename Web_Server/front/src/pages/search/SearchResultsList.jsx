import React from 'react';
import { Searchul, Searchli } from './SearchResults.styled';
import { FormSubTitle } from '../../utils/Form.styled';
import VideoItem from './components/VideoItem';

function SearchResultsList({ results }) {
  return (
    <>
      <FormSubTitle>search results:</FormSubTitle>
      <Searchul>
        {results && results.map((r) => <VideoItem key={r.id} video={r} />)}
      </Searchul>
    </>
  );
}

export default SearchResultsList;
