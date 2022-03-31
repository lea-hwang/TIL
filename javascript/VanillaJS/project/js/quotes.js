const quotes = [
  {
    quote: "There is nothing in the world so irresistibly contagious as laughter and good humor.",
    author: "Charles Dickens",
  },
  {
    quote: "Love does not consist in gazing at each other, but in looking together in the same direction.",
    author: "Antoine de Saint-Exupery",
  },
  {
    quote: "To know is nothing at all; to imagine is everything.",
    author: "Anatole France",
  },
  {
    quote: "The magic of first love is our ignorance that it can ever end.",
    author: "Benjamin Disraeli",
  },
  {
    quote: "Anything you're good at contributes to happiness.",
    author: "Bertrand Russell",
  },
  {
    quote: "Happiness is a warm puppy.",
    author: "Charles M. Schulz",
  },
  {
    quote: "The winds and waves are always on the side of the ablest navigators.",
    author: "Edward Gibbon",
  },
  {
    quote: "The hardest work is to go idle.",
    author: "Jewish proverb(유대인 격언)",
  }
];

const quote = document.querySelector(".quote span:first-child");
const author = document.querySelector(".quote span:last-child");
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;


// Math.random() 0~1 사이의 실수 반환
// Math.round() 반올림
// Math.ceil() 올림
// Math.floor() 버림

// [1,2,3,4].length