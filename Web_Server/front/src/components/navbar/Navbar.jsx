import React from 'react';
import {
  NavContainer,
  NavLink,
  NavLinkContainer,
  NavContentContainer,
} from './Navbar.styled';
import Gear from '../../assets/icons/settings.png';
import Profile from '../../assets/icons/profile.png';
import Logo from '../../assets/icons/logo.png';

function Navbar() {
  return (
    <NavContentContainer>
      <NavContainer>
        <NavLinkContainer className='nav-left'>
          <img className='nav-logo' src={Logo} alt='logo' height={45} />
          <Pages pages={['home', 'search', 'upload']} />
        </NavLinkContainer>
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
    </NavContentContainer>
  );
}

function Pages({ pages }) {
  return (
    <>
      {pages.map((page, index) => {
        return (
          <NavLink href={'/#'} key={page + index}>
            {page}
          </NavLink>
        );
      })}
    </>
  );
}
export default Navbar;
