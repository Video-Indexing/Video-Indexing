import styled, { css } from 'styled-components';

const SectionsContainer = styled.div``;

const Section = styled.section`
  width: 100%;
  height: 500px;
  background-color: ${(props) => props.bg};
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  & .text {
    margin: 2rem;
    padding: 1rem;
    height: calc(100% - 4rem);
    z-index: 1;
    color: white;
  }
  & h1 {
    font-family: 'Poppins';
    font-size: 3.5rem;
  }
  & .image-section {
    max-width: 40%;
  }
`;

const TextContainer = styled.div`
  display: flex;
  justify-content: center;
  flex-direction: column;
`;

const Paragraph = styled.p`
  font-family: 'Rubik';
  font-weight: 400;
  letter-spacing: 0.05em;
  line-height: 2rem;
  font-size: 1.75rem;
  font-weight: 700;
  margin: auto;
  margin: auto;
  &.black {
    color: black;
  }
`;

export { Section, SectionsContainer, Paragraph, TextContainer };
