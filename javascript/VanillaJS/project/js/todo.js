const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input")
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos"
let toDos = [];

function saveToDo(){
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos)); // ["a","b","c"] 형태로 저장됨
}

function deleteToDo(event) {
  const li = event.target.parentElement;    // 현재 선택된 버튼의 부모요소인 li를 선택
  li.remove();                              // 해당 li 삭제
  toDos = toDos.filter(toDo => toDo.id !== parseInt(li.id));  // 해당 todo toDos에서 삭제
  saveToDo()
}


function paintToDo(newToDoObj) {
  const li = document.createElement("li");
  li.id = newToDoObj.id;
  const span = document.createElement("span");
  span.innerText = newToDoObj.text;
  
  const button = document.createElement("button"); // 삭제 버튼
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo); // 버튼을 누르면 해당 todo 삭제

  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li); // 해당 todo todolist에 추가
}

function handleToDoSubmit(event) {
  event.preventDefault();
  const newToDo = toDoInput.value;  // 사용자가 입력한 값 저장
  toDoInput.value = "";             // 입력창 비우기
  const newToDoObj = {
    id:Date.now(),
    text: newToDo,
  };
  toDos.push(newToDoObj);              // toDos 리스트에 저장
  paintToDo(newToDoObj);               // 현재 todo 리스트에 추가
  saveToDo();                       // localstorage에 저장
}

toDoForm.addEventListener("submit", handleToDoSubmit); //제출버튼을 눌렀을 때 실행됨


const savedToDos = localStorage.getItem(TODOS_KEY);  // 로컬 스토리지에 이미 저장되어있는 toDos 불러오기

if (savedToDos !== null) { // 만약 저장되어있는 todo가 존재하다면
  const parsedToDos = JSON.parse(savedToDos);       // 저장되어있는 todo를 리스트 형태로 변환
  toDos = parsedToDos;
  parsedToDos.forEach(paintToDo); // arrow function 화살표 함수
}

// JSON.parse(localStorage.getItem(TODOS_KEY)); // JSON -> list 형태로 바꿔줌

// 화살표 함수
// function sayHello(person){
//   console.log("Hello ", person)
// }
// (person) => console.log("Hello ", person)

// filter function
// function fil(item){
//   return item !== 3;
// }
// [1,2,3,4].filter(fil) //fil 함수에 1, 2, 3, 4를 차례로 넣음