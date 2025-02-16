//1 //условия
// let num = prompt("Введите число:");
// num = Number(num);
// if (num % 2 === 0) {
//     console.log("Число четное");
// } else {
//     console.log("Число нечетное");
// }


//2
// let a = Number(prompt("Введите первое число:"));
// let b = Number(prompt("Введите второе число:"));
// let c = Number(prompt("Введите третье число:"));

// let max = Math.max(a, b, c);
// console.log("Наибольшее число:", max);


//3
// let num = Number(prompt("Введите число:"));

// if (num > 0) {
//     console.log("Число положительное");
// } else if (num < 0) {
//     console.log("Число отрицательное");
// } else {
//     console.log("Число равно нулю");
// }


//4
// let month = Number(prompt("Введите номер месяца (1-12):"));

// if ([12, 1, 2].includes(month)) {
//     console.log("Зима");
// } else if ([3, 4, 5].includes(month)) {
//     console.log("Весна");
// } else if ([6, 7, 8].includes(month)) {
//     console.log("Лето");
// } else if ([9, 10, 11].includes(month)) {
//     console.log("Осень");
// } else {
//     console.log("Некорректный ввод");
// }


//5
// let num = Number(prompt("Введите число:"));
// let isPrime = num > 1;

// for (let i = 2; i <= Math.sqrt(num); i++) {
//     if (num % i === 0) {
//         isPrime = false;
//         break;
//     }
// }

// console.log(isPrime ? "Число простое" : "Число не является простым");






//1 циклы
// let n = Number(prompt("Введите число N:"));
// let sum = 0;

// for (let i = 1; i <= n; i++) {
//     sum += i;
// }

// console.log("Сумма чисел от 1 до", n, "равна", sum);



//2
// for (let i = 2; i <= 100; i += 2) {
//     console.log(i);
// }


//3
// let n = Number(prompt("Введите число N:"));
// let factorial = 1;

// for (let i = 2; i <= n; i++) {
//     factorial *= i;
// }

// console.log("Факториал", n, "равен", factorial);


//4
// let num = Number(prompt("Введите число:"));

// for (let i = 1; i <= 10; i++) {
//     console.log(`${num} × ${i} = ${num * i}`);
// }


//5
// let n = Number(prompt("Введите число N:"));
// let fib = [0, 1];

// for (let i = 2; i < n; i++) {
//     fib.push(fib[i - 1] + fib[i - 2]);
// }

// console.log("Первые", n, "чисел Фибоначчи:", fib.slice(0, n).join(", "));

