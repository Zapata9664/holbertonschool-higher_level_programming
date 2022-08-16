#!/usr/bin/node

function fact (a) {
  if (a > 0) {
    return a * fact(a - 1);
  } else {
    return (1);
  }
}

const a = parseInt(process.argv[2]);
const result = fact(a);
console.log(result);
