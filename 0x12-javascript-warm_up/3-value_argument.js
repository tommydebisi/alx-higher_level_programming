#!/usr/bin/node
// This script prints the first argument passed to it

const newArr = process.argv;

let i = 0;
while (newArr[i]) {
  i++;
}

if (i === 2) {
  console.log('No argument');
} else {
  console.log(newArr[2]);
}
