import React from 'react';
import { NavContainer } from './Navbar.styled';
import Gear from '../../assets/icons/settings.png';
import Profile from '../../assets/icons/profile.png';
import Logo from '../../assets/icons/logo.png';

function Navbar() {
  return (
    <NavContainer>
      <div className='nav-left'>
        <img className='nav-logo' src={Logo} alt='logo' height={45} />
      </div>
      <div className='nav-right'>
        <img
          className='nav-profile'
          src={Profile}
          alt='profile'
          width={35}
          height={35}
        />
        <img
          className='nav-gear'
          src={Gear}
          alt='profile'
          width={35}
          height={35}
        />
      </div>
    </NavContainer>
  );
}

export default Navbar;
