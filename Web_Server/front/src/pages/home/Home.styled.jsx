import styled from 'styled-components';

const SectionsContainer = styled.div``;

const Section = styled.section`
  width: 100%;
  height: 400px;
  background-color: ${(props) => props.bg};
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  & .text {
    margin: 2rem;
    border: 2px solid red;
    width: 100%;
    height: calc(100% - 4rem);
    z-index: 1;
  }
`;

export { Section, SectionsContainer };
