#!/usr/bin/node

const argvCount = process.argv.length;

if (argvCount === 2) {
  console.log('No argument');
} else if (argvCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
