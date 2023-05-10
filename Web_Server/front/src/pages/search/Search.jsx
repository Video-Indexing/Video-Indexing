import React, { useState } from 'react';
import {
  FormContainer,
  FormTitle,
  FormSubTitle,
  FormDivider,
  FormLabel,
  FormInput,
  FormSubmit,
} from '../../utils/Form.styled';
import Searchbar from '../../components/Searchbar/Searchbar';
import SearchResultsList from './SearchResultsList';
import Thumbnail from '../../assets/images/thumbnailex.jpeg';

const resultsex = [
  {
    id: 1,
    title: 'result1',
    image: Thumbnail,
    duration: '2:17',
    chapters: ['ch1', 'ch2'],
  },
  {
    id: 2,
    title: 'result2',
    image: Thumbnail,
    duration: '6:21',
    chapters: ['ch1', 'ch2', 'ch3', 'ch4', 'ch5'],
  },
];

function Search() {
  const [results, setResults] = useState(resultsex);
  const searchResults = (r) => {
    console.log(r);
    setResults(r);
  };
  return (
    <FormContainer>
      <Searchbar setResults={searchResults} />
      <FormDivider />
      {results && <SearchResultsList results={results} />}
    </FormContainer>
  );
}

export default Search;
