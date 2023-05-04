import React, { useState } from 'react';

function PreprocessForm() {
  const [inputText, setInputText] = useState('');
  const [processedText, setProcessedText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('/preprocess/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input_text: inputText }),
    }
    );

    const data = await response.json();
    setProcessedText(data.processed_text);
  };

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Input text:
          </label>
          <input type="text" value={inputText} onChange={handleInputChange} />
        
        <button type="submit">Preprocess</button>
      </form>

      {
      processedText && (
        <div>
          <h2>Processed text:</h2>
          <p>{processedText}</p>
        </div>
      )}
    </div>
  );
}

export default PreprocessForm;
