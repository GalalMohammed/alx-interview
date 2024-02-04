#!/usr/bin/node
const request = require('request');

// Send a GET request to Star wars API
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (_err, _response, body) => {
  printChar(JSON.parse(body).characters, 0);
});
const printChar = (characters, idx) => {
  if (idx < characters.length) {
    request.get(characters[idx], (_err, _response, body) => {
      console.log(JSON.parse(body).name);
      printChar(characters, idx + 1);
    });
  }
};
