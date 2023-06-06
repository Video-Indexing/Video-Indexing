import React from 'react';
import { Section, SectionsContainer } from './Home.styled';
import Section1BG from '../../assets/backgrounds/section-1.jpg';
import Section2BG from '../../assets/backgrounds/section-2.jpg';
import Statistics1 from '../../assets/backgrounds/statistics1.svg';
import Statistics2 from '../../assets/backgrounds/statistics2.svg';
import Statistics3 from '../../assets/backgrounds/statistics3.svg';
import Footer from '../../components/footer/Footer';

function Home() {
  return (
    <>
      <SectionsContainer>
        <Section bg={'#F284FF'}>
          <div className='text'>
            <p>hello</p>
          </div>
          <img src={Section1BG} />
        </Section>
        <Seperator primary={'#F284FF'} secondary={'#ed4bff'} />
        <Section
          bg={'#F2F2F2'}
          style={{ padding: '5%', transform: 'translateY(-10%)', zIndex: '-1' }}
        >
          <Statistics />
          <div className='text'>
            <p>hello</p>
          </div>
        </Section>
        <div style={{ transform: 'rotate(180deg)' }}>
          <Seperator primary={'#DEEAFA'} secondary={'#d0dae8'} />
        </div>
        <Section bg={'#DEEAFA'}>
          <img src={Section2BG} width={750} height={350} />
          <div className='text'>
            <p>hello</p>
          </div>
        </Section>
        <Seperator primary={'#DEEAFA'} secondary={'#d0dae8'} />
        <Section
          bg={'#F2F2F2'}
          style={{ padding: '5%', transform: 'translateY(-10%)', zIndex: '-1' }}
        >
          <div className='text'>
            <p>hello</p>
          </div>
        </Section>
      </SectionsContainer>
    </>
  );
}

function Seperator({ primary, secondary }) {
  return (
    <svg
      style={{ transform: 'translateY(-1%)' }}
      class='separator'
      width='100%'
      height='120'
      viewBox='0.1 0.1 180 40'
      preserveAspectRatio='none'
    >
      <g transform='translate(-18.298844,-77.973964)'>
        <path
          style={{ fill: secondary }}
          d='M 31.615583,86.351641 H 192.16499 v 26.901969 c 0,0 -32.03411,-14.237983 -59.62682,-12.72484 -22.34188,1.2252 -54.779359,9.72634 -54.779359,9.72634 0,0 -22.029534,3.62882 -34.471238,-1.88988 -12.441702,-5.51871 -11.67199,-22.013589 -11.67199,-22.013589 z'
        />
        <path
          style={{ fill: primary }}
          d='M 18.441597,78.106256 H 198.58126 v 39.288614 c 0,0 -43.10672,-27.825245 -73.47599,-19.687823 -30.369264,8.137423 -46.832208,12.548653 -46.832208,12.548653 0,0 -32.775418,8.05972 -46.735258,0 C 17.577964,102.19598 18.441597,78.106256 18.441597,78.106256 Z'
        />
      </g>
    </svg>
  );
}

function Statistics() {
  return (
    <div style={{ position: 'relative', width: '50%', margin: '2rem' }}>
      <img src={Statistics1} height={150} style={{ position: 'absolute' }} />
      <img
        src={Statistics2}
        height={150}
        style={{ position: 'absolute', left: '180px' }}
      />
      <img
        src={Statistics3}
        height={150}
        style={{ position: 'absolute', left: '90px', top: '150px' }}
      />
    </div>
  );
}
export default Home;
