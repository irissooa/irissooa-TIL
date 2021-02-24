'use strict';
import PopUp from './popup.js'

const CARROT_SIZE = 80;
const CARROT_COUNT = 20;
const BUG_COUNT = 20;
const GAME_DURATION_SEC = 20;

const field = document.querySelector('.game__field');
const fieldRect = field.getBoundingClientRect();
const gameBtn = document.querySelector('.game__button');
const gameTimer = document.querySelector('.game__timer');
const gameScore = document.querySelector('.game__score');


const carrotSound = new Audio('./sound/carrot_pull.mp3');
const alertSound = new Audio('./sound/alert.wav');
const bgSound = new Audio('./sound/bg.mp3');
const bugSound = new Audio('./sound/bug_pull.mp3');
const winSound = new Audio('./sound/game_win.mp3');



let started = false;
let score = 0;
let timer = undefined;

const gameFinishBanner = new PopUp();
gameFinishBanner.setClickListener(()=>{
  startGame();
});

field.addEventListener('click', onFiledClick);
gameBtn.addEventListener('click',()=>{
  if (started) {
    stopGame();
  } else {
    startGame();
  }
});

function startGame() {
  started = true;
  initGame();
  showStopButton();
  showTimerAndScore();
  startGameTimer();
  playSound(bgSound);
}
function stopGame() {
  started = false;
  stopGameTimer();
  hideGameButton();
  gameFinishBanner.showWithText('REPLAY?')
  playSound(alertSound);
  stopSound(bgSound);
};

function finishGame(win) {
  started = false;
  hideGameButton();
  if (win) {
    playSound(winSound); 
  } else {
    playSound(bugSound);
  }
  stopGameTimer();
  stopSound(bgSound);
  gameFinishBanner.showWithText(win ? 'YOU WON!' : 'YOU LOST');
};

function showStopButton() {
  const icon = gameBtn.querySelector('.fas');
  icon.classList.add('fa-stop');
  icon.classList.remove('fa-play');
  gameBtn.style.visibility = 'visible';
};

function hideGameButton() {
  gameBtn.style.visibility = 'hidden';
};

function showTimerAndScore() {
  gameTimer.style.visibility = 'visible';
  gameScore.style.visibility = 'visible';
};

function startGameTimer() {
  // setInterval api이용
  // timer를 함수 밖에서도 사용해야되니까 global변수로 사용
  let remainingTimeSec = GAME_DURATION_SEC;
  updateTimerText(remainingTimeSec);
  timer = setInterval(()=>{
    if (remainingTimeSec <= 0) {
      clearInterval(timer);
      finishGame(CARROT_COUNT === score);
      return
    }
    //remainingTimeSec 1초씩 줄어들어야됨
    updateTimerText(--remainingTimeSec)
  },1000);
};

function stopGameTimer() {
  clearInterval(timer);
};

function updateTimerText(time) {
  const minutes = Math.floor(time/60);
  const seconds = time % 60;
  gameTimer.innerText = `${minutes}:${seconds}`
};





function initGame() {
  score = 0;
  field.innerHTML = '';
  gameScore.innerText = CARROT_COUNT;
  // 벌레와 당근을 생성한뒤 field에 추가해줌
  addItem('carrot',CARROT_COUNT,'img/carrot.png');
  addItem('bug',BUG_COUNT,'img/bug.png');
}

function onFiledClick(event) {
  if (!started) {
    return;
  }
  const target = event.target;
  // matches란 함수는 css셀렉터가 해당하는지 확인함
  // carrot클래스를 가진 타겟이면
  if (target.matches('.carrot')) {
    // 당근!
    target.remove();
    score++;
    playSound(carrotSound);
    updateScoreBoard();
    if (score === CARROT_COUNT) {
      finishGame(true);
    }
  } else if(target.matches('.bug')) {
    // 벌레!
    finishGame(false);
  } 
}

function playSound(sound) {
  // 시작을 처음부터하게 설정
  sound.currentTime = 0;
  sound.play();
};

function stopSound(sound) {
  sound.pause();
};

function updateScoreBoard() {
  gameScore.innerText = CARROT_COUNT - score;
}

function addItem(className,count,imgPath) {
  const x1 = 0;
  const y1 = 0;
  // 필드의 끝값에서 당근 사이즈만큼 빼줘야 필드안에 들어감
  const x2 = fieldRect.width-CARROT_SIZE;
  const y2 = fieldRect.height-CARROT_SIZE;
  for (let i = 0; i < count; i++) {
    const item = document.createElement('img');
    item.setAttribute('class',className);
    item.setAttribute('src',imgPath);
    item.style.position = 'absolute';
    const x = randomNumber(x1,x2);
    const y = randomNumber (y1,y2);
    item.style.left = `${x}px`;
    item.style.top = `${y}px`;
    field.appendChild(item); 
  }
}
// 랜덤숫자를 만들어주는 함수
function randomNumber(min,max) {
  return Math.random() * (max-min) + min;
}

initGame();