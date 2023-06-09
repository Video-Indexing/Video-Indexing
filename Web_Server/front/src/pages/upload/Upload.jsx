import React, { useState } from 'react';
import {
  FormContainer,
  FormTitle,
  FormSubTitle,
  FormDivider,
  FormLabel,
  FormInput,
  FormSubmit,
} from '../../utils/Form.styled';
import FormDropDownList from './components/FormDropDownList';
import FormCheckbox from './components/FormCheckbox';
import { UploadVideo, getVideoSubjects } from '../../services/UploadService';

function Upload() {
  const [options, setOptions] = useState();
  React.useEffect(() => {
    const dataFetch = async () => {
      const data = await getVideoSubjects();
      // set state when the data received
      data.topics.push('other');
      setOptions(data.topics);
      setSubjectName(data.topics[0]);
    };
    dataFetch();
  }, []);

  const [titleName, setTitleName] = useState();
  const [subjectName, setSubjectName] = useState();
  const [link, setLink] = useState();
  const [useOriginalTitle, setUseOriginalTitle] = useState(false);
  function onSubmit() {
    UploadVideo(titleName, link);
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
      <FormContainer>
        <FormTitle>Submit A Video</FormTitle>
        <FormSubTitle>Submit your video for evaluation</FormSubTitle>
        <FormDivider />
        <FormLabel>Subject</FormLabel>
        {options && (
          <FormDropDownList options={options} onOptionChange={changeSubject} />
        )}
        <FormLabel>Title</FormLabel>
        <FormInput onChange={(e) => setTitleName(e.target.value)} />
        <FormCheckbox onStateChange={ytTitle}>
          use youtube link title
        </FormCheckbox>
        <FormLabel>Youtube Video Link</FormLabel>
        <FormInput
          className='large'
          onChange={(e) => setLink(e.target.value)}
        />
        <FormSubmit onClick={onSubmit}>Submit</FormSubmit>
      </FormContainer>
    </>
  );
}

export default Upload;
