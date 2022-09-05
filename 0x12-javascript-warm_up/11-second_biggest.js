#!/usr/bin/node
/*
  This script searches the second biggest
  integer in the list of arguments
*/

const newArr = process.argv;

if (newArr.length === 2) {
  console.log(0);
} else if (newArr.length === 3) {
  console.log(0);
} else {
  let max = newArr[2];

  for (let index = 3; index < newArr.length; index++) {
    const argValue = parseInt(newArr[index]);

    if (argValue && argValue > max) {
      max = argValue;
    }
  }

  console.log(max);
}
