const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input")
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos"
const toDos = [];

function saveToDo(){
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos)); // ["a","b","c"] 형태로 저장됨
}

function deleteToDo(event) {
  const li = event.target.parentElement;
  li.remove();
}


function paintToDo(newToDo) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newToDo;
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
  event.preventDefault();
  const newToDo = toDoInput.value;
  toDoInput.value = "";
  toDos.push(newToDo);
  paintToDo(newToDo);
  saveToDo();
}

toDoForm.addEventListener("submit", handleToDoSubmit);


// JSON.parse(localStorage.getItem(TODOS_KEY)); // JSON -> list 형태로 바꿔줌

const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos) {
  const = parsedToDos = JSON.parse(savedToDos);
  parsedToDos.forEach((item) => console.log(item)); // arrow function 화살표 함수
}