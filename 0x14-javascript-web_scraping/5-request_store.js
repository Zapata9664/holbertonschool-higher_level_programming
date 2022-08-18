#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const path = (process.argv[2]);
const file = (process.argv[3])

request.get(path, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  fs.writeFile(file, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
