'use strict';

// export시키면 이 class를 밖으로 노출시키는거다 이파일에서 뿐만아니라 외부에서도 이 클래스를 볼 수 있다
export default class PopUp {
  constructor() {
    this.popUp = document.querySelector('.pop-up');
    this.popUpText = document.querySelector('.pop-up__message');
    this.popUpRefresh = document.querySelector('.pop-up__refresh');
    this.popUpRefresh.addEventListener('click',()=>{
      // 콜백이 있으면 this.onClick이 true
      this.onClick && this.onClick();
      hide();
    })
  }
  // class에 popUp콜백으로 등록해놓을테니 네 팝업에서 버튼이 클릭되면 전달해준 onClick을 호출해라
  setClickListener(onClick) {
    // onClick이라는 멤버변수를 만듦
    this.onClick = onClick;
  }
  
  showWithText(text) {
  this.popUpText.innerText = text;
  this.popUp.classList.remove('pop-up--hide');
}

  hide() {
    this.popUp.classList.add('pop-up--hide');
  }
}