#!/usr/bin/node

if (process.argv[2] == null) {
  console.log('Missing size');
} else if (!isNaN(process.argv[2])) {
  const conv = parseInt(process.argv[2]);
  let iteration = 0;
  const dr = 'X';
  const result = dr.repeat(conv);
  for (iteration; iteration < conv; iteration++) {
    console.log(result);
  }
}
