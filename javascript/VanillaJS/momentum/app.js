// 2-1
//alert("hi");

// 2-2 constant
// 상수
// const a = 1;
// const b = 2;
// const myName = "heewon";

// console.log(a + b);
// console.log("hello " + myName);

// 2-3 variable
// 변수
// let c = 5;
// c = 3;
// console.log(c);

// 2-4 Bolean null undefined
// const isGood = true;
// const isNull = null; // null 형 비어있다는 것을 의미
// let isBad;

// console.log(isGood);
// console.log(isBad); //undefined 아직 할당되지 않은 상태를 의미


// 2-5 Array
// const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];
// const nonsense = [1, 2, "Hello", null, false];

// console.log(daysOfWeek, nonsense);
// console.log(daysOfWeek[0]);

// daysOfWeek.push("sun");

// 2-6 object
// const player = {
//   name: "heewon",
//   points: 10,
// };

// console.log(player.name); // heewon


// 2-7,8 function
// function sayHello(nameOfPerson, age){
//   console.log("Hello my name is " + nameOfPerson + " and I am " + age);
// }

// sayHello("heewon", 25);

// function plus(a, b){
//   console.log(a + b);
// }
// plus(10, 13);

// const player = {
//   name: "heewon",
//   sayHello: function(personName){
//     console.log("hello " + personName + " nice to meet you")
//   },
// }

// console.log(player.name)
// player.sayHello("Lea")

// 2-9,10 recap
// const a = 5; // 변경할 수 없는 변수
// let b = 6; // 변경할 수 있는 변수
// b = 7;

// let a1 = true;  // bool
// let a2 = "ddd"; // text
// let a3 = null;  // nothing, 아직 할당되지 않음, 비어있음
// let a4 = undefined; // 존재하긴 하지만 아예 없음.

// let li = ['a', 'b', 'c']; // array
// console.log(li[1]);
// li.push("d");
// console.log(li);

// const player = {
//   name: "heewon",
//   age: 23,
// };
// player.name = "lea";
// console.log(player);

// function multiply(a, b){ // argument. place holder
//   console.log(a * b);
// }

// multiply(2, 4);

// const calculator = {
//   plus: function(a, b){ console.log(a + b) },
//   multiply: function(a, b){ console.log(a * b) },
//   minus: function(a, b){ console.log(a - b) },
//   devide: function(a, b){ console.log(a / b) },
//   power: function(a, b){ console.log(a ** b) },
// }

// calculator.plus(1, 2);
// calculator.multiply(1, 2);
// calculator.minus(1, 2);
// calculator.devide(1, 2);
// calculator.power(1, 2);

// 2-11,12
// const age = 25;
// function calculateAmAge(myAge) {
//   return myAge -2;
// }

// const amAge = calculateAmAge(age);

// console.log(amAge);

// // 2-13
// const age = prompt("How old are you?"); // 프롬포트 창으로 사용자에게 입력값을 받는다. 굉장히 오래된 방범.


// //console.log(typeof age, typeof parseInt(age)); // typeof는 변수의 타입을 반환
// console.log(age, parseInt(age)); // NaN는 'Not a Number'라는 의미
// parseInt(); // parseInt("")문자 타입을 숫자 타입으로 변경

// 2-14,15 conditionals
// const age = parseInt(prompt("How old are you?")); // 프롬포트 창으로 사용자에게 입력값을 받는다. 굉장히 오래된 방범.

// // isNaN(); // isNan()은 숫자인지 NaN인지 여부 확인

// if(isNaN(age)){ //if 조건문, ()안의 조건문이 참일 때 실행
//   console.log("Please write a number");
// } else if (age < 18) {
//   console.log("You are too young");
// } else if (age >= 18 && age < 50) { // && : and ||: or
//   console.log("You can drink.")
// } else if (age >= 50 && age < 80){
//     console.log("You are too old to drink.");
// } else {
//     console.log("You can do whatever you want.");
// }

// if (age === 101){
//   console.log("you are good");
// } else if (age !== 101){
//   console.log("you are also good");
// }

// 3-1

// document //html을 자바스크립트 관점에서 볼 수 있음. html에서 작성된 부분을 자바스크립트에서 받아서 사용할 수 있음
// console.log(document.title)
// document.title = "Hi";
// document.body;

// // 3-2
// const title = document.getElementById("title");
// console.dir(title);

// title.innerText = "Hello!";

// console.log(title.id);
// console.log(title.className); // Html의 element를 가져올 수 있음.

// 3-3

const Hellos = document.getElementsByClassName("hello");
console.log(Hellos);

const title = document.querySelector(".hello hi"); // selector
const titles = document.querySelectorAll(".hello hi"); // selector
