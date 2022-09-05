#!/usr/bin/node
/*
  script that prints My number: <first argument converted in integer>
  if the first argument can be converted to an integer
*/

const newArr = process.argv;
let newInt;

if (newArr.length === 2) {
  console.log('Not a number');
} else {
  newInt = parseInt(newArr[2]);
  if (newInt) {
    console.log(`My number: ${newInt}`);
  } else {
    console.log('Not a number');
  }
}
