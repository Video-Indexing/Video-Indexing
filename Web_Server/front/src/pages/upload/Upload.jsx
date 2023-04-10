import React, { useState } from 'react';
import {
  FormContainer,
  FormTitle,
  FormSubTitle,
  FormDivider,
  FormLabel,
  FormInput,
  FormSubmit,
} from './Upload.stlyed';
import Navbar from '../../components/navbar/Navbar';

function Upload() {
  const [titleName, setTitleName] = useState();
  const [subjectName, setSubjectName] = useState();
  const [link, setLink] = useState();

  function onSubmit() {
    console.log(
      `title: ${titleName}\nsubject: ${subjectName}\nyt-link: ${link}`
    );
  }

  return (
    <>
      <Navbar />
      <FormContainer>
        <FormTitle>Submit A Video</FormTitle>
        <FormSubTitle>Submit your video for evaluation</FormSubTitle>
        <FormDivider />
        <FormLabel>Title</FormLabel>
        <FormInput onBlur={(e) => setTitleName(e.target.value)} />
        <FormLabel>Subject</FormLabel>
        <FormInput onBlur={(e) => setSubjectName(e.target.value)} />
        <FormLabel>Youtube Video Link</FormLabel>
        <FormInput
          className='yt-link'
          onBlur={(e) => setLink(e.target.value)}
        />
        <FormSubmit onClick={onSubmit}>Submit</FormSubmit>
      </FormContainer>
    </>
  );
}

export default Upload;
