#!/usr/bin/node

const path = (process.argv[2]);
const quote = (process.argv[3]);
const fs = require('fs');
fs.writeFile(path, quote, 'utf8', function (err, data) {
  if (err) {
    return (console.log(err));
  }
});
