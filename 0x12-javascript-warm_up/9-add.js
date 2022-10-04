#!/usr/bin/node

const intOne = Number(process.argv[2]);
const intTwo = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

if (intOne && intTwo) {
  add(intOne, intTwo);
} else {
  console.log('NaN');
}
