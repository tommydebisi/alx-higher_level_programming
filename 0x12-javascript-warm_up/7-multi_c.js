#!/usr/bin/node
/*
  This script prints x times “C is fun”
  Where x is the first argument of the script
*/

const newArr = process.argv;
let newInt;

if (newArr.length === 2) {
  console.log('Missing number of occurrences');
} else {
  newInt = parseInt(newArr[2]);
  if (newInt) {
    while (newInt > 0) {
      console.log('C is fun');
      newInt--;
    }
  }
}
