const clock = document.querySelector(".clock");


function getClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2,"0");
  const minutes = String(date.getMinutes()).padStart(2,"0");
  const seconds = String(date.getSeconds()).padStart(2,"0");
  clock.innerText = `${hours}:${minutes}:${seconds}`;
}

getClock(); // 처음에 한번 호출
setInterval(getClock, 1000); //1000ms마다 호출

//setInterval(sayHello, 5000); // 5000ms 마다 sayHello가 실행되도록 함

// setTimeout(sayHello, 5000); // 5000ms 기다렸다가 sayHello 실행

// const date = new Date();
// date.getDate();
// date.getHours();
// date.getMinutes();
// date.getSeconds();
// new Date().getSeconds();

// "1".padStart(2, "0"); // 만약 해당 문자가 길이가 2가 아닐 경우 0을 앞에 채운다.
// "2".padEnd(2, "0"); // 뒤에 0추가
// String(1); // 숫자를 문자로 바꿈