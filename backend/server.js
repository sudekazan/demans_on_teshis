const express = require('express');
const cors = require('cors');
require('dotenv').config();

const connectDB = require('./config/db');
const sessionRoutes = require('./routes/sessionRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Connect Database
connectDB();

// Health Check
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', message: 'Demans Backend API operational', timestamp: new Date() });
});

// Routes
app.use('/api/sessions', sessionRoutes);

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`[Express Backend] Listening on http://localhost:${PORT}`);
  });
}

module.exports = app;
