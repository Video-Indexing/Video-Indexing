import styled from 'styled-components';

const NavContainer = styled.div`
  width: 100vw;
  min-height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #434343;
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

export { NavContainer };
