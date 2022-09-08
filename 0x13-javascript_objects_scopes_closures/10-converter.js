#!/usr/bin/node

/*
  This script converts a number from base 10 to
  another base passed as argument:
*/

exports.converter = function (base) {
  return function (number) {
    return Number(number).toString(base);
  };
};
