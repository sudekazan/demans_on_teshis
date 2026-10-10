const mongoose = require('mongoose');

const connectDB = async () => {
  if (process.env.NODE_ENV === 'test') return;
  try {
    const connStr = process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/demans_db';
    const conn = await mongoose.connect(connStr, { serverSelectionTimeoutMS: 2000 });
    console.log(`[MongoDB] Connected: ${conn.connection.host}`);
  } catch (error) {
    console.warn(`[MongoDB Warning] Could not connect to local MongoDB. Operating in mock memory mode.`);
  }
};

module.exports = connectDB;
