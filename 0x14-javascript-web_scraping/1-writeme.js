#!/usr/bin/node

const fs = require('fs');
const path = (process.argv[2]);
const quote = (process.argv[3]);
fs.writeFile(path, quote, (err) => {
  if (err) {
    console.error(err);
  }
});
