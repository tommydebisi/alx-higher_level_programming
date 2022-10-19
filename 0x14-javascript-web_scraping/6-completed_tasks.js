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

  // care less about sorting
  for (const todo of todos) {
    if (todo.completed) {
      if (newObj[todo.userId]) {
        newObj[todo.userId] += 1;
      } else {
        newObj[todo.userId] = 1;
      }
    }
  }
  console.log(newObj);
});
