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
import { Outlet, Link } from 'react-router-dom';

function Navbar() {
  const selected = () => {
    const split = window.location.href.split('/');
    return split[split.length - 1];
  };
  const [page, setPage] = React.useState(selected());
  function Pages({ pages }) {
    return (
      <>
        {pages.map((p, index) => {
          return (
            <NavLink
              key={index}
              className={`${p === page && 'current'} shrink-border`}
            >
              <Link to={p} key={p + index} onClick={() => setPage(p)}>
                {p}
              </Link>
            </NavLink>
          );
        })}
        <Outlet />
      </>
    );
  }
  return (
    <NavContentContainer>
      <NavContainer>
        <NavLinkContainer className='nav-left'>
          <img
            className='nav-logo'
            src={Logo}
            alt='logo'
            height={45}
            onClick={() => window.location.replace(`home`)}
          />
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

export default Navbar;
