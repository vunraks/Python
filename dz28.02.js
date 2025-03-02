//1
// function compareNumbers(a, b) {
//     return a < b ? -1 : a > b ? 1 : 0;

// }
// console.log(compareNumbers(5, 10));
// console.log(compareNumbers(10, 5));
// console.log(compareNumbers(7, 7));


//2
// function factorial(n) {
//     return n <= 1 ? 1 : n * factorial(n - 1);
// }
// console.log(factorial(5));


//3
// function mergeDigits(a, b, c) {
//     return parseInt(`${a}${b}${c}`);
// }
// console.log(mergeDigits(1, 4, 9));


//4
// function calcArea(length, width = length) {
//     return length * width;
// }
// console.log(calcArea(5, 10));
// console.log(calcArea(4));


//5
// function isPerfectNumber(n) {
//     let sum = 0;
//     for (let i = 1; i < n; i++) {
//         if (n % i === 0) sum += i;
//     }
//     return sum === n;
// }
// console.log(isPerfectNumber(6));
// console.log(isPerfectNumber(28));
// console.log(isPerfectNumber(12));


//6
// function findPerfectNumbersInRange(min, max) {
//     let result = [];
//     for (let i = min; i <= max; i++) {
//         if (isPerfectNumber(i)) result.push(i);
//     }
//     return result;
// }
// console.log(findPerfectNumbersInRange(1, 1000));


//7
// function formatTime(hours, minutes = 0, seconds = 0) {
//     return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
// }
// console.log(formatTime(9, 5, 3));
// console.log(formatTime(12));


//8
// function timeToSeconds(hours, minutes, seconds) {
//     return hours * 3600 + minutes * 60 + seconds;
// }
// console.log(timeToSeconds(1, 1, 1));


//9
// function secondsToTime(seconds) {
//     let h = Math.floor(seconds / 3600);
//     let m = Math.floor((seconds % 3600) / 60);
//     let s = seconds % 60;
//     return formatTime(h, m, s);
// }
// console.log(secondsToTime(3661));


//10
// function dateDifference(h1, m1, s1, h2, m2, s2) {
//     let time1 = timeToSeconds(h1, m1, s1);
//     let time2 = timeToSeconds(h2, m2, s2);
//     let diff = Math.abs(time1 - time2);
//     return secondsToTime(diff);
// }
// console.log(dateDifference(14, 30, 0, 12, 15, 20));



