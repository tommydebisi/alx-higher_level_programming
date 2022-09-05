#!/usr/bin/node

/*
  This script computes and prints a factorial
*/

function factorial (num) {
  if (num < 2) {
    return (1);
  }

  return (num * factorial(num - 1));
}

const newArr = process.argv;

if (newArr.length === 2) {
  console.log(1);
} else {
  const firstInt = parseInt(newArr[2]);

  console.log(factorial(firstInt));
}
