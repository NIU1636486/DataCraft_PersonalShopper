import React, { useEffect, useState } from 'react';
import ClotheCard from '../components/ClotheCard';

interface SelectionData {
  selectionID: number;
  userID: number;
  shopperID: number;
  approved: string;
  clothes: {
    id: number;
    name: string;
    url: string; // New attribute
  }[];
}

function UserPurchases() {
  const [userIdInput, setUserIdInput] = useState<number>(4); // Default user ID
  const [selectionData, setSelectionData] = useState<SelectionData | null>(null);
  const [buttonStates, setButtonStates] = useState<{ [key: number]: boolean }>({});
  const [overallApproval, setOverallApproval] = useState<string>('');

  useEffect(() => {
    const apiUrl = `http://localhost:8000/selection/${userIdInput}`;

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setSelectionData(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, [userIdInput]);

  useEffect(() => {
    // Check if any button is pressed
    const isAnyButtonPressed = Object.values(buttonStates).some(value => value);

    // Set overall approval status
    setOverallApproval(isAnyButtonPressed ? 'Declined' : 'Approved');
  }, [buttonStates]);

  const handleButtonClick = (clotheId: number, newState: boolean) => {
    setButtonStates(prevStates => ({ ...prevStates, [clotheId]: newState }));
  };

  const handleSaveClick = () => {
    if (selectionData) {
      const updatedClothes = selectionData.clothes.filter(clothe => !buttonStates[clothe.id]);
      const updatedSelectionData: SelectionData = {
        ...selectionData,
        approved: overallApproval,
        clothes: updatedClothes,
      };

      // Make a PUT request to update the data
      const apiUrl = `http://localhost:8000/selection/${selectionData.selectionID}`;
      fetch(apiUrl, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedSelectionData),
      })
        .then(response => response.json())
        .then(data => {
          // Reset the state and update UI
          setSelectionData(null);
          setButtonStates({});
          setOverallApproval('');
        })
        .catch(error => {
          console.error('Error updating data:', error);
        });
    }
  };

  return (
    <div style={{ padding: '50px' }}>
      <div style={{ marginBottom: '20px' }}>
        <label>
          User ID:
          <input
            type="number"
            value={userIdInput}
            onChange={e => setUserIdInput(Number(e.target.value))}
            style={{ marginLeft: '10px', width: "50px"}}
          />
        </label>
      </div>

      {selectionData && selectionData.approved === 'Waiting' ? (
        <>
          <h2 style={{ paddingBottom: '10px' }}>Your new selection</h2>
          <div style={{ display: 'flex', flexWrap: 'wrap' }}>
            {selectionData.clothes.map(clothe => (
              <ClotheCard
                key={clothe.id}
                src={clothe.url}
                title={clothe.name}
                isButtonPressed={buttonStates[clothe.id] || false}
                onButtonClick={newState => handleButtonClick(clothe.id, newState)}
              />
            ))}
          </div>
          <button
            onClick={handleSaveClick}
            style={{
              backgroundColor: 'blue',
              color: 'white',
              padding: '12px',
              borderRadius: '5px',
              marginTop: '20px',
              width: '90px',
              maxWidth: '300px',
              marginLeft: '95%',
            }}
          >
            Save
          </button>
        </>
      ) : (
        <>
          <h2 style={{ paddingBottom: '10px' }}>No new selections</h2>
        </>
      )}
    </div>
  );
}

export default UserPurchases;
