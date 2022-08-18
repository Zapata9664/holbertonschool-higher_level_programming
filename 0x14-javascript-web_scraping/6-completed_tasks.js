#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const Dict = JSON.parse(body);

  const user = {};
  let completed = 0;
  let prevUser = 1;

  for (const i of Dict) {
    if (prevUser !== i.userId) {
      prevUser = i.userId;
      completed = 0;
    }
    if (i.completed) {
      completed++;
      user[i.userId] = completed;
    }
  }

  console.log(user);
});