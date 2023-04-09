import styled from 'styled-components';

const NavContainer = styled.div`
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  & * {
    margin: 0 0.25rem;
    cursor: pointer;
  }
  & .nav-profile {
    transition: 0.25s ease-in-out;
  }
  & .nav-profile:hover {
    transform: scale(1.1);
  }
  & .nav-gear {
    transition: 0.25s ease-in-out;
  }
  & .nav-gear:hover {
    transform: scale(1.1) rotate(90deg);
  }
  & .nav-logo {
    margin: 0.25rem;
  }
`;

const NavContentContainer = styled.div`
  width: 100vw;

  border-bottom: 1px solid #434343;
`;

const NavLink = styled.p`
  padding: 0 5px;
  color: #838383;

  &:hover {
    text-decoration: underline;
  }
`;

const NavLinkContainer = styled.div`
  display: inline-flex;
  align-items: center;
  justify-content: space-around;
`;
export { NavContainer, NavLink, NavLinkContainer, NavContentContainer };
