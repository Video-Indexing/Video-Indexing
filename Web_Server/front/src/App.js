import Navbar from '../src/components/navbar/Navbar.jsx';
import './assets/global.css';
import Upload from './pages/upload/Upload.jsx';
import Signup from './pages/signup/Signup.jsx';
import Search from './pages/search/Search.jsx';
import { useState } from 'react';
import { Routes, Route, BrowserRouter, Link } from 'react-router-dom';
import Homepage from './pages/upload/home/Homepage.jsx';
import PlayVideo from './pages/playVideo/PlayVideo.jsx';

function App() {
  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
            <Route index element={<Homepage />} />
            <Route path="upload" element={<Upload />} />
            <Route path="search" element={<Search />} />
            <Route path="playVideo/*" element={<PlayVideo />} />
            {/* <Route path="*" element={<NoPage />} /> */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
