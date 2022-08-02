#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const myVar = process.argv.slice(2);
const numb = parseInt(myVar[0], 10);
const numb2 = parseInt(myVar[1], 10);
console.log(add(numb, numb2));
