import React from 'react';
import { FormSelect } from '../../../utils/Form.styled';
import { FormInput } from '../../../utils/Form.styled';
import Cancel from '../../../assets/icons/cancel.png';

function FormDropDownList({ options, onOptionChange }) {
  const [value, setValue] = React.useState();
  const [textMode, setTextMode] = React.useState(false);
  const handleChange = (e) => {
    const value = e.target.value;
    if (value === 'other') {
      setTextMode(true);
      return;
    }
    setValue(value);
    onOptionChange(value);
  };
  return (
    <>
      {textMode ? (
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <FormInput
            onChange={(e) => onOptionChange(e.target.value)}
          ></FormInput>
          <img
            className='action'
            src={Cancel}
            height={20}
            onClick={() => setTextMode(false)}
            style={{ cursor: 'pointer' }}
          />
        </div>
      ) : (
        <FormSelect value={value} onChange={handleChange}>
          {options.map((o, index) => (
            <option value={o} key={index + 1}>
              {o}
            </option>
          ))}
        </FormSelect>
      )}
    </>
  );
}
export default FormDropDownList;
