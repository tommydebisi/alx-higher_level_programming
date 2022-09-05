#!/usr/bin/node
// This script prints a message depending of the number of arguments

const newArr = process.argv;

if (newArr.length === 2) {
  console.log('No argument');
} else if (newArr.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
