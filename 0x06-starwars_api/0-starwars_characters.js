#!/usr/bin/node
const request = require('request');

// Send a GET request to Star wars API
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (_err, _response, body) => {
  for (const character of JSON.parse(body).characters) {
    request.get(character, (_err, _response, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});
