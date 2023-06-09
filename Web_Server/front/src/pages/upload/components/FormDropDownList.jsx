import React from 'react';
import { FormSelect } from '../../../utils/Form.styled';
import { getVideoSubjects } from '../../../services/UploadService';

function FormDropDownList({ options, onOptionChange }) {
  const addExist = React.useRef(
    options.push({ label: 'Other', value: 'other' })
  );
  React.useEffect(() => {
    console.log(getVideoSubjects());
  });
  const [value, setValue] = React.useState();
  const handleChange = (e) => {
    const value = e.target.value;
    setValue(value);
    onOptionChange(value);
  };
  return (
    <FormSelect value={value} onChange={handleChange}>
      {options.map((option, index) => (
        <option value={option.value} key={index + 1}>
          {option.label}
        </option>
      ))}
    </FormSelect>
  );
}
export default FormDropDownList;
