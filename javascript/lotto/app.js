const button = document.querySelector('#lottoButton')
const sevenNums = _.sampleSize(_.range(1, 46), 7)
const lottoNums = _.orderBy(sevenNums.slice(0, 6))
const bonusNum = sevenNums[6]

// lottoNums.push(bonusNum) 
const lottoBallList = getBalls(lottoNums)
const bunusBallList = getBalls([bonusNum])

const lottoBalls = document.querySelector('#lottoBalls')
const bonusBall = document.querySelector('#bonusBall')
lottoBalls.append(lottoBallList)
bonusBall.append()




function selectBallColor(num) {
  if (_.inRange(num, 1, 11)){
    return '#E3A816'
  } else if (_.inRange(num, 11, 21)) {
    return '#69C8F2'
  } else if (_.inRange(num, 21, 31)) {
    return '#E96352'
  } else if (_.inRange(num, 31, 41)) {
    return '#8F8F8F'
  } else {
    return '#5AB544'
  }
}

function getSixNumber(){
  return _.orderBy(_.sampleSize(_.range(1, 46), 6))
}

function getBalls(pickedNums){
  const ballList = document.createElement('div')
  ballList.classList.add('ball-list')
  pickedNums.forEach(ballNum => {
    const ballTag = document.createElement('div')
    ballTag.classList.add('ball')
    ballTag.innerText = ballNum
    ballTag.style.backgroundColor = selectBallColor(ballNum)
    ballList.append(ballTag)
  });
  return ballList
}

function compareWithLotto(pickedNums){
  let sameLottoNum = 0
  let sameBonusNum = 0
  pickedNums.forEach((num)=>{
    if (num in lottoNums) {
      sameLottoNum += 1
    }
    if (num === bonusNum) {
      sameBonusNum += 1
    }
  })

  if (sameLottoNum === 6){
    return '1등당첨'
  } else if (sameLottoNum === 5 && sameBonusNum === 1) {
    return '2등당첨'
  } else if (sameLottoNum === 5) {
    return '3등당첨'
  } else if (sameLottoNum === 4) {
    return '4등당첨'
  } else if (sameLottoNum === 3) {
    return '5등당첨'
  } else {
    return '꽝'
  }
}

function playLotto(){
  const section = document.querySelector('#result')
  const tbody = document.querySelector('table tbody')
  const trs = tbody.querySelectorAll('tr')
  const fiveLotto = ['A', 'B', 'C', 'D', 'E']
  section.classList.remove('d-none')

  trs.forEach((tr, index)=>{
    const pickedNums = getSixNumber()              // 뽑은 여섯개 숫자
    const turn = document.createElement('th')      // 다섯번 turn
    const winOrLose = document.createElement('td') // 당첨여부
    const sixBalls = document.createElement('td')  // 선택한 공

    turn.innerText = fiveLotto[index]
    winOrLose.innerText = compareWithLotto(pickedNums)
    sixBalls.append(getBalls(pickedNums))

    while (tr.firstChild) {
      tr.removeChild(tr.firstChild);
    }

    tr.append(turn)
    tr.append(winOrLose)
    tr.append(sixBalls)

  })
  
}


button.addEventListener('click', playLotto)
