#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, 'utf-8', (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
