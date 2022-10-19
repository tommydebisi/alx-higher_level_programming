#!/usr/bin/node
// This script computes the number of tasks completed by user id.
const request = require('request');

const url = process.argv[2];

request(url, 'utf-8', (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const todos = JSON.parse(body);
  const newObj = {};
  let uId = todos[0].userId;
  newObj[uId] = 0;

  for (const todo of todos) {
    if (uId !== todo.userId) {
      newObj[todo.userId] = 0;
      uId = todo.userId;
    }

    if (todo.completed === true) {
      newObj[todo.userId] += 1;
    }
  }
  console.log(newObj);
});
