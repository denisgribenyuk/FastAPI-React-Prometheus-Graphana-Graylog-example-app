import React, { useState } from 'react';
import ItemList from './ItemList';
import ItemDetail from './ItemDetail';

const App = () => {
  const [selectedItemId, setSelectedItemId] = useState(null);

  const handleSelectItem = (itemId) => {
    setSelectedItemId(itemId);
  };

  return (
    <div className="App">
      <ItemList onSelectItem={handleSelectItem} />
      {selectedItemId && <ItemDetail itemId={selectedItemId} />}
    </div>
  );
};

export default App;
