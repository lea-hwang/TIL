const images = [
  {
    author: "Ricardo Gomez Angel",
    authorLink: "https://unsplash.com/@rgaleria?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
    photo: "img0.jpg",
    photoLink: "https://unsplash.com/s/photos/swiss-field?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
  },
  {
    author: "Vitaliy Gavrushchenko",
    authorLink: "https://unsplash.com/@gavrushchenko?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
    photo: "img1.jpg",
    photoLink: "https://unsplash.com/s/photos/field?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
  },
  {
    author: "Tom Shakir",
    authorLink: "https://unsplash.com/@digitalcontentkings?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
    photo: "img2.jpg",
    photoLink: "https://unsplash.com/s/photos/peaceful?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText",
  },
];

const background = document.querySelector(".background")
const chosenImage = images[Math.floor(Math.random() * images.length)];
const backgroundImage = document.createElement("img");  // img라는 새로운 태그를 생성하려고 함.
const photoAuthor = document.querySelector(".background span a:first-child");
const photoLink = document.querySelector(".background span a:last-child");

// background 수정
backgroundImage.src = `img/${chosenImage.photo}`;       // img 태그의 src값 변경
background.appendChild(backgroundImage);                // 해당 태그를 body의 child에 넣음.
photoAuthor.innerText = chosenImage.author;             // 태그 내부 글자 변경
photoAuthor.href = chosenImage.authorLink;              // href 속성값 변경
photoLink.href = chosenImage.photoLink;

// prependChild 부모태그 내부에서, 제일 앞쪽(위쪽)에 새로운 child를 삽입. 