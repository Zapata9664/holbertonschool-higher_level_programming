#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let iterator = 0;
  let count = 0;
  for (iterator; iterator < list.length; iterator++) {
    if (list[iterator] === searchElement) {
      count += 1;
    }
  }
  return (count);
};
