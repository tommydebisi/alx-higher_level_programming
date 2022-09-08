#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

// for .. of loop is used for arrays
for (const [key, val] of Object.entries(dict)) {
  if (newDict[val]) {
    newDict[val].push(key);
  } else {
    newDict[val] = [key];
  }
}

console.log(newDict);
