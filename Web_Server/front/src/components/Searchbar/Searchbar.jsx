import React, { useState } from 'react';
import { Bar, SearchInput } from './Searchbar.styled';
import Search from '../../assets/icons/search.png';
import Cancel from '../../assets/icons/cancel.png';

function Searchbar({ setResults }) {
  const [search, setSearch] = useState();
  const clear = () => {
    document.getElementById('search').value = '';
    setSearch(null);
  };
  const query = (e) => {
    const searchQuery = document.getElementById('search').value;
    console.log(`query: ${searchQuery}\nkey words: ${searchQuery.split(' ')}`);
    const searchResults = searchQuery.split(' '); // make firebase fetch request
    setResults(searchResults);
  };
  return (
    <>
      <Bar>
        <img className='action' src={Search} height={18} onClick={query} />
        <SearchInput
          id='search'
          type='text'
          placeholder='Search'
          onChange={(e) => setSearch(e.target.value)}
        />
        {search && (
          <img className='action' src={Cancel} height={20} onClick={clear} />
        )}
      </Bar>
    </>
  );
}

export default Searchbar;
