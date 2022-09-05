#!/usr/bin/node
/*
  This script searches the second biggest
  integer in the list of arguments
*/

// remove args 0 and 1
const newArr = process.argv.slice(2);

const integers = newArr.filter(arg => !isNaN(arg));
const numbers = integers.map(arg => parseInt(arg)); // convert args to int

let largest = 0;
if (numbers.length > 1) {
  largest = Math.max(...numbers); // get max value

  numbers.splice(numbers.indexOf(largest), 1);
  largest = Math.max(...numbers);
}

console.log(largest);
