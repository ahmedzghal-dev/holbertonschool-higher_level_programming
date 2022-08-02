#!/usr/bin/node
const { argv } = require('process');
const n = parseInt(argv[2]);

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
