#!/usr/bin/node
/*
  This script that prints the addition of 2 integers
*/

function add (a, b) {
  return (a + b);
}

const newArr = process.argv;

if (newArr.length === 2) {
  console.log('NaN');
} else if (newArr.length === 3) {
  console.log('NaN');
} else {
  const firstInt = parseInt(newArr[2]);
  const secondInt = parseInt(newArr[3]);

  console.log(add(firstInt, secondInt));
}
