#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' + (process.argv[2]);

request(url, function (err, response) {
  if (err) {
    console.log(err);
  }
  const save = (JSON.parse(response.body).title);
  console.log(save);
});
