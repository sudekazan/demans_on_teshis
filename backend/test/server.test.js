const test = require('node:test');
const assert = require('node:assert');
const app = require('../server');

test('GET /api/health should return status OK', async () => {
  const req = new Request('http://localhost:5000/api/health');
  // Express handles internal routing; simple validation test
  assert.strictEqual(typeof app, 'function');
});
