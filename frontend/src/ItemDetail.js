import React, { useEffect, useState } from 'react';
import { fetchItemById } from './api';
import { Card, CardContent, Typography } from '@mui/material';

const ItemDetail = ({ itemId }) => {
  const [item, setItem] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchItemById(itemId);
      console.log(data);
      setItem(data);
    };

    if (itemId) {
      fetchData();
    }
  }, [itemId]);

  if (!item) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Item Detail</h2>
      <Card>
        <CardContent>
          <Typography variant="h5" component="div">
            ID: {item.id}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Title: {item.title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Description: {item.description}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Description: {item.created_date}
          </Typography>
          {/* Добавьте другие поля объекта по вашему усмотрению */}
        </CardContent>
      </Card>
    </div>
  );
};

export default ItemDetail;
