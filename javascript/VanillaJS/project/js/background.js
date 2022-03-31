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



// const backgroundImage = document.querySelector(".background img");
// const author = document.querySelector(".background span a:first-child");
// const photo = document.querySelector(".background span a:last-child");
const chosenImage = images[Math.floor(Math.random() * images.length)].photo;
const backgroundImage = document.createElement("img");
backgroundImage.src = `img/${chosenImage}`;
document.body.appendChild(backgroundImage);
// author.innerText = chosenImage.author;
// author.href = chosenImage.authorLink;
// photo.href = chosenImage.photoLink;



  