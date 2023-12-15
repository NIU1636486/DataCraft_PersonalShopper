import React, { useState, useEffect } from 'react';
import ClotheCard from '../components/ClotheCardNew';

interface Clothe {
  id: number;
  name: string;
  url: string;
}

interface SelectionData {
  selectionID: number;
  userID: number;
  shopperID: number;
  approved: string;
  clothes: Clothe[];
}

const ShopperNewSelection: React.FC = () => {
  const [userNumber, setUserNumber] = useState<number>(1);
  const [clothes, setClothes] = useState<Clothe[]>([]);
  const [selectedClothes, setSelectedClothes] = useState<number[]>([]);
  const [selectionID, setSelectionID] = useState<number | null>(null);

  useEffect(() => {
    fetch('http://localhost:8000/clothes/all')
      .then((response) => response.json())
      .then((data: Clothe[]) => setClothes(data))
      .catch((error) => console.error('Error fetching clothes:', error));
  }, []);

  useEffect(() => {
    fetch('http://localhost:8000/selection/')
      .then((response) => response.json())
      .then((data: SelectionData[]) => setSelectionID(data.length + 1))
      .catch((error) => console.error('Error fetching selection ID:', error));
  }, []);

  const handleUserNumberChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUserNumber(parseInt(event.target.value, 10));
  };

  const handleButtonClick = (clotheID: number) => {
    setSelectedClothes((prevSelected) =>
      prevSelected.includes(clotheID)
        ? prevSelected.filter((id) => id !== clotheID)
        : [...prevSelected, clotheID]
    );
  };

  const resetClothesSelection = () => {
    setSelectedClothes([]);
  };

  const handleSubmit = () => {
    const selectionData: SelectionData = {
      selectionID: selectionID!,
      userID: userNumber,
      shopperID: 1, // You may need to change this based on your requirements
      approved: 'pending', // You may need to change this based on your requirements
      clothes: clothes.filter((clothe) => selectedClothes.includes(clothe.id)),
    };

    fetch('http://localhost:8000/selection/new_selection', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(selectionData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('New selection created:', data);
        resetClothesSelection(); // Reset clothes selection after successful submission
      })
      .catch((error) => console.error('Error creating new selection:', error));
  };

  return (
    <div style={{ padding: '50px' }}>
      <label>
        User ID:
        <input
          type="number"
          value={userNumber}
          onChange={handleUserNumberChange}
          style={{ marginLeft: '5px', width: '50px', marginBottom: '40px' }}
        />
      </label>
      <div style={{ display: 'flex', flexDirection: 'row' }}>
        {clothes.map((clothe) => (
          <ClotheCard
            key={clothe.id}
            src={clothe.url}
            title={clothe.name}
            isButtonPressed={selectedClothes.includes(clothe.id)}
            onButtonClick={() => handleButtonClick(clothe.id)}
          />
        ))}
      </div>
      <button
        onClick={handleSubmit}
        style={{
          marginTop: '20px',
          marginLeft: '95%',
          backgroundColor: 'blue',
          color: 'white',
          padding: '12px',
          borderRadius: '5px',
          width: '90px',
          maxWidth: '300px',
        }}
      >
        Enviar
      </button>
    </div>
  );
};

export default ShopperNewSelection;
