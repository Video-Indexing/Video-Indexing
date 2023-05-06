import Navbar from '../src/components/navbar/Navbar.jsx';
import './assets/global.css';
import Upload from './pages/upload/Upload.jsx';
import Signup from './pages/signup/Signup.jsx';
import Searchbar from './components/Searchbar/Searchbar.jsx';
function App() {
  return (
    <>
      <Navbar />
      <Signup />
      <Searchbar />
    </>
  );
}

export default App;
