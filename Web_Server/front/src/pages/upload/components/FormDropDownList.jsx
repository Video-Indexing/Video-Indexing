import React from 'react';
import { FormSelect } from '../Upload.stlyed';

function FormDropDownList({ options, onOptionChange }) {
  const [value, setValue] = React.useState();
  const handleChange = (e) => {
    const value = e.target.value;
    setValue(value);
    onOptionChange(value);
  };

  return (
    <FormSelect value={value} onChange={handleChange}>
      {options.map((option, index) => (
        <option value={option.value} key={index}>
          {option.label}
        </option>
      ))}
    </FormSelect>
  );
}
export default FormDropDownList;
