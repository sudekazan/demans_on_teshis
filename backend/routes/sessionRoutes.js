const express = require('express');
const router = express.Router();
const Session = require('../models/Session');

// In-memory fallback array for dev without live MongoDB
const memorySessions = [];

/**
 * @route   POST /api/sessions
 * @desc    Record a new cognitive test session anonymously
 */
router.post('/', async (req, res) => {
  try {
    const { user_uuid, test_type, metrics, context } = req.body;

    if (!user_uuid || !test_type || !metrics) {
      return res.status(400).json({ error: 'Missing required parameters (user_uuid, test_type, metrics)' });
    }

    const sessionData = {
      user_uuid,
      test_type,
      timestamp: new Date(),
      metrics,
      context: context || { fatigue_score: 2, time_of_day: 'day' },
    };

    // Save to Mongo if connected, otherwise memory
    try {
      const newSession = new Session(sessionData);
      await newSession.save();
    } catch (e) {
      memorySessions.push(sessionData);
    }

    res.status(201).json({
      success: true,
      message: 'Cognitive test session saved anonymously',
      data: sessionData,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * @route   GET /api/sessions/:user_uuid
 * @desc    Get all test sessions for a given anonymous UUID
 */
router.get('/:user_uuid', async (req, res) => {
  try {
    const { user_uuid } = req.params;
    let list = [];

    try {
      list = await Session.find({ user_uuid }).sort({ timestamp: -1 });
    } catch (e) {
      list = memorySessions.filter(s => s.user_uuid === user_uuid);
    }

    res.json({
      success: true,
      count: list.length,
      data: list,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
