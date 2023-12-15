import React, { useEffect, useState } from 'react';
import ClotheCardNoButton from '../components/ClotheCardNoButton';

interface SelectionData {
  selectionID: number;
  userID: number;
  shopperID: number;
  approved: string;
  clothes: {
    id: number;
    name: string;
    url: string;
  }[];
}

function getColorAndText(approved: string) {
  const color = (approved === 'Waiting') ? 'blue' :
                (approved === 'Approved') ? 'green' :
                (approved === 'Declined') ? 'red' : 'blue'; 
  return { color, text: approved === 'Waiting' ? 'Esperant' : (approved === 'Approved' ? 'Aprovat' : 'Denegat') };
}

function ShopperSelections() {
  const [selectionList, setSelectionList] = useState<SelectionData[]>([]);

  useEffect(() => {
    const apiUrl = 'http://localhost:8000/selection/';

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setSelectionList(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div style={{ padding: '50px' }}>
      {selectionList.map(selectionData => (
        <div style={{ marginBottom: '40px' }} key={selectionData.selectionID}>
            <div style={{display: "flex"}}>
            <h2 style={{ paddingBottom: '5px' , display:"block", width: "250px"}}>Compra per {selectionData.userID}</h2>
            <button
                style={{
                backgroundColor: 'transparent',
                color: getColorAndText(selectionData.approved).color,
                border: `1px solid ${getColorAndText(selectionData.approved).color}`,
                borderRadius: '4px',
                padding: '8px',
                marginBottom: "10px",
                width: '100px',

                }}
            >
                {getColorAndText(selectionData.approved).text}
            </button>
            </div>
          <div style={{ display: 'flex', flexWrap: 'wrap' }}>
            {selectionData.clothes.map(clothe => (
              <ClotheCardNoButton key={clothe.id} src={clothe.url} title={clothe.name} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default ShopperSelections;
