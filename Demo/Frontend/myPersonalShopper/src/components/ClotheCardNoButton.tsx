import React from 'react';

interface ImageCardProps {
  src: string;
  title: string;
}

const ClotheCard: React.FC<ImageCardProps> = ({ src, title }) => {
  return (
    <div style={{ textAlign: 'center', width: '200px', height: '270px', border: '1px solid #ccc', padding: '10px', marginRight: '30px', borderRadius: '8px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <img src={src} alt={title} style={{ width: '100%', height: 'auto', borderRadius: '8px' }} />
      </div>
      <div>
        <h6 style={{ textAlign: "left" }}>{title}</h6>
      </div>
    </div>
  );
};

export default ClotheCard;