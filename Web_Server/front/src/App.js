import Navbar from '../src/components/navbar/Navbar.jsx';
import './assets/global.css';
import Upload from './pages/upload/Upload.jsx';
import Signup from './pages/signup/Signup.jsx';
import Search from './pages/search/Search.jsx';
import { useState } from 'react';
import Homepage from './pages/upload/home/Homepage.jsx';

function App() {
  return (
    <>
      <Navbar />
      <Search />
    //   return <Homepage />
    </>
  );
}

export default App;
