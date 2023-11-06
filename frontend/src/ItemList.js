import React, { useState, useEffect } from 'react';
import { fetchItems } from './api';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const ItemList = ({ onSelectItem }) => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchItems();
      setItems(data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Item List</h2>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Title</TableCell>
              {/* Добавьте другие заголовки по вашему усмотрению */}
            </TableRow>
          </TableHead>
          <TableBody>
            {items.map((item) => (
              <TableRow style={{ cursor: 'pointer' }} key={item.id} onClick={() => onSelectItem(item.id)}>
                <TableCell>{item.id}</TableCell>
                <TableCell>{item.title}</TableCell>
                {/* Добавьте другие ячейки данных по вашему усмотрению */}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default ItemList;
