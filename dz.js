//1
// let start = parseInt(prompt("Введите начальное число:"));
// let end = parseInt(prompt("Введите конечное число:"));
// let sum = 0;

// for (let i = start; i <= end; i++) {
//     sum += i;
// }

// console.log("Сумма чисел:", sum)

//2
// let a = parseInt(prompt("Введите первое число:"));
// let b = parseInt(prompt("Введите второе число:"));

// while (b != 0) {
//     let temp = b;
//     b = a % b;
//     a = temp;
// }
// console.log("НОД:", a);


//3
// let num = parseInt(prompt("Введите число:"));

// console.log("Делители числа:");
// for (let i = 1; i <= num; i++) {
//     if(num % i === 0) {
//         console.log(i);
//     }
// }

//4
// let number = Math.abs(parseInt(prompt("Введите число:")));
// let count = 0;
// while (number>0){
//     number = Math.floor(number / 10);
//     count++;
// }
// console.log("Количество цифр в числе:", count);


//5
// let positive = 0, negative = 0, zeros = 0, even = 0, odd = 0;

// for (let i = 0; i < 10; i++) {
//     let num = parseInt(prompt(`Введите число ${i + 1}:`));

//     if (num > 0) positive++;
//     else if (num < 0) negative++;
//     else zeros++;

//     if (num % 2 === 0) even++;
//     else odd++;
// }

// console.log(`Положительных: ${positive}, Отрицательных: ${negative}, Нулей: ${zeros}`);
// console.log(`Четных: ${even}, Нечетных: ${odd}`);


//6
// do {
//     let num1 = parseFloat(prompt("Введите первое число:"));
//     let num2 = parseFloat(prompt("Введите второе число:"));
//     let operator = prompt("Введите оператор (+, -, *, /):");
//     let result;

//     switch (operator) {
//         case "+": result = num1 + num2; break;
//         case "-": result = num1 - num2; break;
//         case "*": result = num1 * num2; break;
//         case "/": result = num2 !== 0 ? num1 / num2 : "Ошибка (деление на 0)"; break;
//         default: result = "Неверный оператор";
//     }

//     console.log("Результат:", result);
// } while (confirm("Хотите решить еще один пример?"));



//7
// let num = prompt("Введите число:");
// let shift = parseInt(prompt("Введите сдвиг вправо:")) % num.length;

// let result = num.slice(shift) + num.slice(0, shift);

// console.log("Результат:", result);


//8
// const days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"];
// let index = 0;

// do {
//     console.log(days[index]);
//     index = (index + 1) % days.length;
// } while (confirm("Хотите увидеть следующий день?"));


//9
// for (let i = 2; i <= 9; i++) {
//     console.log(`\nТаблица умножения для ${i}:`);
//     for (let j = 1; j <= 10; j++) {
//         console.log(`${i} × ${j} = ${i * j}`);
//     }
// }


//10
// alert("Загадайте число от 0 до 100, а я попробую его угадать!");
// let min = 0;
// let max = 100;
// let guess;
// let response;

// while (true) {
//     guess = Math.floor((min + max) / 2);
//     response = prompt(`Ваше число > ${guess}, < ${guess} или == ${guess}? (Введите >, < или ==)`);

//     if (response === "==") {
//         alert(`Я угадал! Ваше число: ${guess}`);
//         break;
//     } else if (response === ">") {
//         min = guess + 1;
//     } else if (response === "<") {
//         max = guess - 1;
//     }
// }
