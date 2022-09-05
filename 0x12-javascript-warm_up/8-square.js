#!/usr/bin/node
/*
  This script prints a square of length x
  Where x is the first argument of the script
*/

const newArr = process.argv;

if (newArr.length === 2) {
  console.log('Missing size');
} else {
  const newInt = parseInt(newArr[2]);

  if (newInt) {
    for (let i = 0; i < newInt; i++) {
      let squareContent = '';
      for (let j = 0; j < newInt; j++) {
        squareContent += 'X';
      }
      console.log(squareContent);
    }
  } else {
    console.log('Missing size');
  }
}
