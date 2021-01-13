const { expect } = require('chai');
const request = require('request');

describe('API 8', () => {
  it('request', () => {
    request('http://localhost:7865', (error, response, body) => {
      if (response) {
        expect(body).to.equals('Welcome to the payment system');
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
      }
    });
  });
});
