#!/usr/bin/node

const size = Number(process.argv[2]);

if (size) {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let c = 0; c < size; c++) line += 'X';
    console.log(line);
  }
} else {
  console.log('Missing size');
}
