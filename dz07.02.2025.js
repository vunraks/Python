const CURRENT_YEAR = 2024;
const EXCHANGE_RATE = 0.92; // Пример курса доллара к евро
const FILE_SIZE_MB = 820;

// Запрос имени
let name = prompt("Введите ваше имя:");
alert(`Привет, ${name}!`);

// Запрос года рождения и расчет возраста
let birthYear = prompt("Введите ваш год рождения:");
let age = CURRENT_YEAR - birthYear;
alert(`Вам ${age} лет.`);

// Периметр квадрата
let squareSide = prompt("Введите длину стороны квадрата:");
let perimeter = squareSide * 4;
alert(`Периметр квадрата: ${perimeter}`);

// Площадь окружности
let radius = prompt("Введите радиус окружности:");
let circleArea = Math.PI * radius * radius;
alert(`Площадь окружности: ${circleArea.toFixed(2)}`);

// Расчет скорости
let distance = prompt("Введите расстояние между городами (км):");
let time = prompt("За сколько часов хотите добраться?");
let speed = distance / time;
alert(`Необходимая скорость: ${speed.toFixed(2)} км/ч`);

// Конвертор валют
let dollars = prompt("Введите сумму в долларах:");
let euros = dollars * EXCHANGE_RATE;
alert(`Сумма в евро: ${euros.toFixed(2)}`);

// Рассчет количества файлов на флешке
let flashSizeGB = prompt("Введите объем флешки (Гб):");
let filesCount = Math.floor((flashSizeGB * 1024) / FILE_SIZE_MB);
alert(`На флешку поместится ${filesCount} файлов размером 820 Мб.`);

// Покупка шоколадок
let money = prompt("Введите сумму денег в кошельке:");
let chocolatePrice = prompt("Введите цену одной шоколадки:");
let chocolates = Math.floor(money / chocolatePrice);
let change = money % chocolatePrice;
alert(`Вы можете купить ${chocolates} шоколадок. Сдача: ${change.toFixed(2)}`);

// Обратный порядок числа
let number = prompt("Введите трехзначное число:");
let reversedNumber = number.split('').reverse().join('');
alert(`Число задом наперед: ${reversedNumber}`);

// Проверка на четность
let intNumber = prompt("Введите целое число:");
alert(intNumber % 2 === 0 ? "Число четное" : "Число нечетное");
