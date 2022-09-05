#!/usr/bin/node
/*
  This script prints two arguments passed to it
  in the following format: “ is ”
*/

const newArr = process.argv;

if (newArr.length === 2) {
  console.log('undefined is undefined');
} else if (newArr.length === 3) {
  console.log(`${newArr[2]} is undefined`);
} else {
  console.log(`${newArr[2]} is ${newArr[3]}`);
}
