#!/usr/bin/node

let countDown = 0;
exports.logMe = function (item) {
  console.log(`${countDown++}: ${item}`);
};
