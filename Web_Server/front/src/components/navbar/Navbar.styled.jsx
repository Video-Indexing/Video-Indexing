import styled from 'styled-components';

const NavContainer = styled.div`
  width: 100vw;
  min-height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid black;
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
`;

export { NavContainer };
