#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const myDict = JSON.parse(body);

  const user = {};
  let UserPrevious = 1;
  let comp = 0;

  for (const i of myDict) {
    if (UserPrevious !== i.userId) {
        UserPrevious = i.userId;
      comp = 0;
    }
    if (i.comp) {
      comp++;
      user[i.userId] = comp;
    }
  }

  console.log(user);
});
