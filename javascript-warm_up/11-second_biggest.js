#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const second = args.find(n => n < args[0]) || 0;
  console.log(second);
}
