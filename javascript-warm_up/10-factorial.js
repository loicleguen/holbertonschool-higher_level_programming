#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function fact (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(arg));
