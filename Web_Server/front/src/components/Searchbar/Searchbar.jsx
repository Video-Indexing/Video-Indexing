import React, { useState } from 'react';
import { Bar, SearchInput } from './Searchbar.styled';
import Search from '../../assets/icons/search.png';
import Cancel from '../../assets/icons/cancel.png';

function Searchbar() {
  const [search, setSearch] = useState();
  const clear = () => (document.getElementById('search').value = '');
  return (
    <>
      <Bar>
        <img className='action' src={Search} height={18} />
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
