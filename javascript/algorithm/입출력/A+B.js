// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value)
// const [a,b] = input
// console.log(a+b)

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const A = parseInt(input[0]);
const B = parseInt(input[1]);
console.log(A + B);