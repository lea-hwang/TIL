const API_KEY = ''
const searchBoxInput = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')
let albumPage = 1

function fetchAlbums(page=1, limit=10){
  const keyword = searchBoxInput.value
  const URL = `http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&api_key=${API_KEY}&limit=${limit}&page=${page}&format=json`
  loadingList.setAttribute('style', 'display:block;')

  axios.get(URL)
  .then(res => {
    const albums = res.data.results.albummatches.album
    albums.forEach((album)=> {
      const card = document.createElement('div')
      const img = document.createElement('img')
      const text = document.createElement('div')
      const artistName = document.createElement('h2')
      const albumName = document.createElement('p')

      card.classList.add('search-result__card')
      img.src = album.image[1]['#text']
      artistName.innerText = album.artist
      albumName.innerText = album.name

      searchResult.append(card)
      card.append(img)
      card.append(text)
      text.append(artistName)
      text.append(albumName)

      card.addEventListener('click', function(){
        window.location.href = album.url
      })
    })
    loadingList.setAttribute('style', 'display:none;')
  })
  .catch(err => { alert('잠시 후 다시 시도해주세요') })
}


searchBtn.addEventListener('click', (event)=>{
  event.preventDefault()
  while(searchResult.firstChild){
    searchResult.firstChild.remove()
  }
  fetchAlbums(albumPage, 30)
})


document.addEventListener('scroll', (event)=>{
  if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
    albumPage += 1
    fetchAlbums(albumPage, 30)
  }
})
