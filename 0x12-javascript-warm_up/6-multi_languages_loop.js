#!/usr/bin/node
/*
  This script prints 3 lines: (like 1-multi_languages.js) but
  by using an array of string and a loop
*/

const newArr = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

for (let index = 0; index < newArr.length; index++) {
  console.log(newArr[index]);
}
