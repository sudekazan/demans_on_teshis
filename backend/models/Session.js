const mongoose = require('mongoose');

const SessionSchema = new mongoose.Schema({
  user_uuid: {
    type: String,
    required: true,
    index: true,
  },
  test_type: {
    type: String,
    enum: ['STROOP', 'VISUAL_MEMORY', 'DIGIT_SPAN'],
    required: true,
  },
  timestamp: {
    type: Date,
    default: Date.now,
  },
  metrics: {
    mean_rt_ms: Number,
    std_dev_ms: Number,
    accuracy: Number,
    correct_count: Number,
    total_trials: Number,
    max_digit_span: Number,
    raw_reaction_times: [Number],
  },
  context: {
    fatigue_score: { type: Number, default: 2 },
    time_of_day: { type: String, default: 'day' },
  },
});

module.exports = mongoose.model('Session', SessionSchema);
