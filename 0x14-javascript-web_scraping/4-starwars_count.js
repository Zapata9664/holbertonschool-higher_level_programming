#!/usr/bin/node

const request = require('request');
const path = process.argv[2];
let count = 0;

request(path, function (err, response) {
  if (err) {
    return console.log(err);
  }
  const save = (JSON.parse(response.body));

  for (const pel in save.results) {
    for (const actor in (save.results[pel].characters)) {
      const url = (save.results[pel].characters[actor]).split('/');
      if (url[5] === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
