import styled from 'styled-components';

const ItemContainer = styled.div`
  display: flex;
  padding: 0.5rem 0;
  border-bottom: 1px solid lightgray;
  gap: 0.25rem;
  cursor: pointer;

  &:first-child {
    border-top: 1px solid lightgray;
  }
`;

const VideoDescription = styled.div`
  display: flex;
  height: 100%;
  width: 100%;
  margin: 0.25rem;
  flex-direction: column;
  align-items: baseline;
  justify-content: space-between;
`;

const ItemTitle = styled.div`
  font-size: 1.1rem;
  text-decoration: underline;
  margin-bottom: 0.3rem;
`;

const ItemChapters = styled.div`
  display: flex;
  gap: 0.25rem;
  & p {
    font-size: 0.75rem;
  }
  & p:hover {
    cursor: pointer;
    text-decoration: underline;
  }
`;

const ItemP = styled.p`
  font-size: 0.75rem;
  font-weight: light;
`;

export { ItemContainer, ItemTitle, VideoDescription, ItemChapters, ItemP };
