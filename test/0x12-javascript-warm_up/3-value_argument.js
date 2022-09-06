#!/usr/bin/node

const argvOne = process.argv[2];
if (argvOne === undefined) {
  console.log('No argument');
} else {
  console.log(argvOne);
}
