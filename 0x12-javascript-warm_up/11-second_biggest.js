#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log('0');
} else {
  const na = process.argv.sort((a, b) => a - b);
  console.log(na[na.length - 2]);
}
