#!/usr/bin/node
// This script prints the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film in films) {
    for (const character in films[film].characters) {
      if (films[film].characters[character].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
