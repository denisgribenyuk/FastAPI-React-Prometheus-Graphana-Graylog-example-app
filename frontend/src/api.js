import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const API_HOST = process.env.APP_HOST || 'localhost';
const API_PORT = process.env.APP_PORT || 8000;

const API_URL = `http://${API_HOST}:${API_PORT}`;

export const fetchItems = async () => {
  try {
    const response = await axios.get(`${API_URL}/items`);
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    return [];
  }
};

export const fetchItemById = async (itemId) => {
  try {
    const response = await axios.get(`${API_URL}/items/${itemId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching item by ID:', error);
    return null;
  }
};
