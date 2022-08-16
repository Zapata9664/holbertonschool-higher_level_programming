#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  const conv = parseInt(process.argv[2]);
  let iteration = 0;
  const dr = 'X';
  const result = dr.repeat(conv);
  for (iteration; iteration < conv; iteration++) {
    console.log(result);
  }
} else {
  console.log('Missing size');
}
