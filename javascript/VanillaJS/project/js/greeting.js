const loginForm = document.querySelector(".login-form");
const loginInput = document.querySelector(".login-form input");
// const link = document.querySelector("a");
const greeting = document.querySelector(".greeting");

// string들은 따로 저장해두는 것이 좋음. 
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";

function onLoginSubmit(event) { // event 정보가 담김
  event.preventDefault(); //preventDefault() 브라우저의 동작을 막음
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  paintGreetings(username);
  //removeItem, setItem, getItem
}

// function handleLinkClick(event){
//   event.preventDefault(); // default behavior가 실행되지 않음.

// }

// loginForm.addEventListener("submit", onLoginSubmit);
// onLoginSubmit 이라는 이름만 주고 바로 실행되지 않는다.
// onLoginSubmit()라고 작성하면 즉시 실행하는 것을 의미한다

// link.addEventListener("click", handleLinkClick)
function paintGreetings(username){
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}


const savedUsername = localStorage.getItem(USERNAME_KEY);
if (savedUsername === null) { // 저장된 유저네임 값이 없을 경우,
  // form 보여주기
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  paintGreetings(savedUsername);
}