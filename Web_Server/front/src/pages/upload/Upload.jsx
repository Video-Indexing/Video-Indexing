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
import FormDropDownList from './components/FormDropDownList';
import FormCheckbox from './components/FormCheckbox';
import Navbar from '../../components/navbar/Navbar';

function Upload() {
  const options = [
    { label: 'Optimizers', value: 'optimizers' },
    { label: 'Embedding', value: 'embedding' },
  ];
  const [titleName, setTitleName] = useState();
  const [subjectName, setSubjectName] = useState(options[0]);
  const [link, setLink] = useState();
  const [useOriginalTitle, setUseOriginalTitle] = useState(false);
  function onSubmit() {
    console.log(
      `title: ${titleName}\nsubject: ${subjectName}\nyt-link: ${link}\nytTitle: ${useOriginalTitle}`
    );
  }
  const changeSubject = (value) => setSubjectName(value);
  const ytTitle = (value) => {
    setUseOriginalTitle(value);
  };

  return (
    <>
      <Navbar />
      <FormContainer>
        <FormTitle>Submit A Video</FormTitle>
        <FormSubTitle>Submit your video for evaluation</FormSubTitle>
        <FormDivider />
        <FormLabel>Subject</FormLabel>
        <FormDropDownList options={options} onOptionChange={changeSubject} />
        <FormLabel>Title</FormLabel>
        <FormInput onBlur={(e) => setTitleName(e.target.value)} />
        <FormCheckbox onStateChange={ytTitle}>
          use youtube link title
        </FormCheckbox>
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
