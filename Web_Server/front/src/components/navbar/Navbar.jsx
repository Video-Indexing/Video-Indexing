import React from 'react';
import { NavContainer } from './Navbar.styled';
import Gear from '../../assets/icons/settings/settings.png';
import GearAnimation from '../../assets/icons/settings/settings.gif';
import Profile from '../../assets/icons/profile.png';
import '../../assets/icons/settings/settings.css';

function Navbar() {
  return (
    <NavContainer>
      <div className='nav-left'></div>
      <div className='nav-right'>
        <img
          className='nav-profile'
          src={Profile}
          alt='profile'
          width={35}
          height={35}
        />
        <SettingsGear width={35} height={35} />
      </div>
    </NavContainer>
  );
}

function SettingsGear({ width, height }) {
  return (
    <>
      <img
        src={Gear}
        alt='settings'
        className='static'
        width={width}
        height={height}
      />
      <img
        src={GearAnimation}
        alt='settings'
        className='active'
        width={width}
        height={height}
      />
    </>
  );
}

export default Navbar;
