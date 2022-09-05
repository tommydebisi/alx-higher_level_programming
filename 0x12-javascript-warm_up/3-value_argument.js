#!/usr/bin/node
// This script prints the first argument passed to it

const newArr = process.argv;

if (newArr.length === 2) {
  console.log('No argument');
} else {
  console.log(newArr[2]);
}
