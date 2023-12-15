import React, { useState } from 'react';

interface ImageCardProps {
  src: string;
  title: string;
  isButtonPressed: boolean;
  onButtonClick: (newState: boolean) => void;
}

const ClotheCard: React.FC<ImageCardProps> = ({ src, title, isButtonPressed, onButtonClick }) => {
  const handleButtonClick = () => {
    onButtonClick(!isButtonPressed);
  };

  return (
    <div style={{ textAlign: 'center', width: '200px', height: '270px', border: '1px solid #ccc', padding: '10px', marginRight: '30px', borderRadius: '8px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
      <img src={src} alt={title} style={{ width: '100%', height: 'auto', borderRadius: '8px' }} />
    </div>
    <div>
      <h6 style={{ textAlign: "left" }}>{title}</h6>
      <button
        style={{
          backgroundColor: isButtonPressed ? 'blue' : 'transparent',
          color: isButtonPressed ? 'white' : 'blue',
          border: '1px solid blue',
          borderRadius: '4px',
          padding: '8px',
          cursor: 'pointer',
          width: "100%",
        }}
        onClick={handleButtonClick}
      >
        {isButtonPressed ? 'Selected' : 'Select'}
      </button>
    </div>
  </div>
  );
};

export default ClotheCard;