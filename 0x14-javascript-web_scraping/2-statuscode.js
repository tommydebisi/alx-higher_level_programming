#!/usr/bin/node
// This script display the status code of a GET request.
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});
