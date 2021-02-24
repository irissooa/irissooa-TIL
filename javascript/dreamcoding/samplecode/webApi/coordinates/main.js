const vertical = document.querySelector('.vertical');
const horizontal = document.querySelector('.horizontal');
const target = document.querySelector('.target');
const tag = document.querySelector('.tag');

// 성능 개선 전
// document.addEventListener('mousemove', (event)=>{
//   const x = event.clientX;
//   const y = event.clientY;

//   vertical.style.left = `${x}px`;
//   horizontal.style.top = `${y}px`;
//   target.style.left = `${x}px`;
//   target.style.top = `${y}px`;
//   tag.style.left = `${x}px`;
//   tag.style.top = `${y}px`;
//   tag.innerHTML = `${x}px, ${y}px`;
// })

//성능 개선 후
addEventListener('load',()=>{

  const targetRect = target.getBoundingClientRect();
  const targetHalfWidth = targetRect.width /2;
  const targetHalfHeight = targetRect.height /2;

  document.addEventListener('mousemove', (event)=>{
    const x = event.clientX;
    const y = event.clientY;

    vertical.style.transform = `translateX(${x}px)`;
    horizontal.style.transform =`translateY(${y}px)`;
    target.style.transform = `translate(${x - targetHalfWidth}px,${y - targetHalfHeight}px)`;
    tag.style.transform = `translate(${x + 20}px,${y + 20}px)`;
    tag.innerHTML = `${x}px, ${y}px`;
  })

  
})