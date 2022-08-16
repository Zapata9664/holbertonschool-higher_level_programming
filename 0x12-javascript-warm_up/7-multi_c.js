#!/usr/bin/node

function print () {
  if (process.argv[2] == null) {
    console.log('Missing number of occurrences');
  } else if (!isNaN(process.argv[2])) {
    const conv = parseInt(process.argv[2]);
    let iteration = 0;
    for (iteration; iteration < conv; iteration++) {
      console.log('C is fun');
    }
  }
}
print();
