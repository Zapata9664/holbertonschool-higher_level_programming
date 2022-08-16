#!/usr/bin/node

function add (a, b) {
  const suma = a + b;
  return suma;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const result = add(a, b);
console.log(result);
