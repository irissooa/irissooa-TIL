// 필요한 DOM요소 정의
const items = document.querySelector('.items');
const input = document.querySelector('.footer__input');
const addBtn = document.querySelector('.footer__button');

// 함수
// click을 하는 함수는 보통 'on'으로 시작함
function onAdd() {
  // 1. 사용자가 입력한 텍스트를 받아옴
  const text = input.value;
  // 사용자가 입력하지 않으면 focus만 하고 return
  if (text === '') {
    input.focus();
    return;
  }
  // 2. 새로운 아이템을 만듦(텍스트 + 삭제 버튼)
  const item = createItem(text);
  // 3. items 컨테이너 안에 새로 만든 아이템을 추가
  items.appendChild(item);
  // 4. 새로 추가된 아이템으로 스크롤링
  item.scrollIntoView({block:'center'});
  // 5. input 초기화 함
  input.value = ''
  // focus를 줘야 추가할 수 있음 아니면 마우스로 input창 클릭해야됨
  input.focus();
}

function createItem(text) {
  const itemRow = document.createElement('li');
  itemRow.setAttribute('class','item__row');

  const item = document.createElement('div');
  item.setAttribute('class','item');
  
  const name = document.createElement('span');
  name.setAttribute('class','item__name');
  name.innerText = text;

  const deleteBtn = document.createElement('button');
  deleteBtn.setAttribute('class','item__delete');
  deleteBtn.innerHTML = '<i class="fas fa-trash-alt"></i>';
  deleteBtn.addEventListener('click',()=>{
    items.removeChild(itemRow);
  })

  const itemDivider = document.createElement('div');
  itemDivider.setAttribute('class','item__divider');

  item.appendChild(name);
  item.appendChild(deleteBtn);

  itemRow.appendChild(item);
  itemRow.appendChild(itemDivider);
  
  return itemRow;
}
addBtn.addEventListener('click',()=>{
  onAdd();
})

input.addEventListener('keypress',(event)=>{
  if (event.key === 'Enter') {
    onAdd();
  }
})