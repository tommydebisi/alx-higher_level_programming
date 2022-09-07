#!/usr/bin/node

// This script returns the reversed version of a list:

exports.esrever = function (list) {
  const arrNew = [];

  for (let i = list.length - 1; i >= 0; i--) {
    arrNew.push(list[i]);
  }
  return arrNew;
};
