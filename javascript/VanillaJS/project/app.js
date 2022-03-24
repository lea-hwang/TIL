const loginForm = document.querySelector(".login-form")
const loginInput = document.querySelector(".login-form input");
const link = document.querySelector("a")

function onLoginSubmit(event) { // event 정보가 담김
  event.preventDefault(); //preventDefault() 브라우저의 동작을 막음
  console.log(loginInput)
}

function handleLinkClick(event){
  event.preventDefault(); // default behavior가 실행되지 않음.
  alert("clicked")
}

loginForm.addEventListener("submit", onLoginSubmit);
// onLoginSubmit 이라는 이름만 주고 바로 실행되지 않는다.
// onLoginSubmit()라고 작성하면 즉시 실행하는 것을 의미한다

link.addEventListener("click", handleLinkClick)

