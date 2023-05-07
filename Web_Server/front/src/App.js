import Navbar from '../src/components/navbar/Navbar.jsx';
import './assets/global.css';
import Upload from './pages/upload/Upload.jsx';
import Signup from './pages/signup/Signup.jsx';
import Search from './pages/search/Search.jsx';
import { useState } from 'react';

function App() {
  return (
    <>
      <Navbar />
      <Search />
    </>
  );
}

export default App;
