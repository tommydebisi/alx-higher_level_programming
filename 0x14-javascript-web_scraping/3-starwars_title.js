#!/usr/bin/node
// This script prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
