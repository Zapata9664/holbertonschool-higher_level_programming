#!/usr/bin/node

const count= require('console');
const request = require('request')
const path = 'https://swapi-api.hbtn.io/api/' + process.argv[2];
request.get(url, function(error, response, body) {
  if (err) {
    console.err(err);
  }

  const url = JSON.parse(body).results;
  const iterator = 0;
  const iteradorDos = 0;
  for (iterator; iterator < path.length; iterator++) {
    for (iteradorDos; iteradorDos < url[iterator].characters.length; iteradorDos++) {
        if (path[iterator].characters[iteradorDos].endsWith('18/')) {
            count++;
        }
    }
  }
  console.log(count);
});