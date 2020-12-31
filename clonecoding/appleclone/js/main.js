// 즉시호출 함수를 만듦!, 배열에 스크롤에 대한 정보를 다 넣어줌!
// 전역변수 사용을 피하기 위해 즉시호출함수이용
(() => {
// 변수 생성
	let yOffset = 0; // window.pageYOffset 대신 쓸 변수(상황에 따라 바로 쓸수도 있지만, 따로 조작한 뒤, 값을 쓰기 위해 변수를 만듦)
	let prevScrollHeight = 0; // 현재 스크롤 위치(yOffset)보다 이전에 위치한 스크롤 섹션들의 스크롤 높이값의 합
	let currentScene = 0; // 현재 활성화된(눈 앞에 보고있는) 씬(scroll-section)
	let enterNewScene = false; // 새로운 scene이 시작된 순간 true
	// 부드러운 감속 비디오에 적용하기 위한 변수
	let acc = 0.2;
	let delayedYOffset = 0;
	let rafId;
	let rafState;
// 각 scene에 대한 정보를 담을 배열
	const sceneInfo = [
		{
			// 0
			// 스크롤구간에 sticky
			type: 'sticky',
			heightNum: 5, // 브라우저 높이의 5배로 scrollHeight 세팅(각 디바이스마다 높이가 다르기때문에 그 해당 디바이스높이에 5배할거란 말)
			scrollHeight: 0,//스크롤높이(다른 함수로 높이 설정을 해줄거야, 이걸 스크롤 높이의 몇배수로 적용하기 위해, 바로 적용안힘, 창 사이즈 변경에도 대응해야되기 때문에 따로 함수 처리)
			// 각 섹션의 html정보를 넣음
			// 조작할 dom객체를 잡아둠
			objs: {
				container: document.querySelector('#scroll-section-0'),
				// 0번 섹션안에 main-message의a클래스 라고 적어줘야됨!아니면 헷갈림
				messageA: document.querySelector('#scroll-section-0 .main-message.a'),
				messageB: document.querySelector('#scroll-section-0 .main-message.b'),
				messageC: document.querySelector('#scroll-section-0 .main-message.c'),
				messageD: document.querySelector('#scroll-section-0 .main-message.d'),
				// canvas, context를 가져옴
				canvas: document.querySelector('#video-canvas-0'),
				context: document.querySelector('#video-canvas-0').getContext('2d'),
				// 이미지 순서 수백장을 여기에 넣을 예정
				videoImages: []
			},
			// 변화를 줄 obj마다 어떤값을 줄지 적어줌
			values: {
				// 이미지 개수,
				videoImageCount: 300,
				// 이미지 순서 변화,[초기값, 끝값]
				imageSequence: [0, 299],
				// 투명도와 translateY를 조절해줘야됨
				// 마지막에 사라질때 자연스럽게 사라지게하기위해 적용
				canvas_opacity: [1, 0, { start: 0.9, end: 1 }],
				// 투명도 시작값, 끝값, 타이밍(객체를 넣음, 소수점인 이유는 비율이기때문)
				// 들어가고(스크롤 위에서 아래로 내려감)
				messageA_opacity_in: [0, 1, { start: 0.1, end: 0.2 }],
				messageB_opacity_in: [0, 1, { start: 0.3, end: 0.4 }],
				messageC_opacity_in: [0, 1, { start: 0.5, end: 0.6 }],
				messageD_opacity_in: [0, 1, { start: 0.7, end: 0.8 }],
				// 살짝 위로 올라옴 자기높이의 20%만큼 살짝 올라감
				messageA_translateY_in: [20, 0, { start: 0.1, end: 0.2 }],
				messageB_translateY_in: [20, 0, { start: 0.3, end: 0.4 }],
				messageC_translateY_in: [20, 0, { start: 0.5, end: 0.6 }],
				messageD_translateY_in: [20, 0, { start: 0.7, end: 0.8 }],
				// 나가고(스크롤 아래에서 위로 올라감)
				messageA_opacity_out: [1, 0, { start: 0.25, end: 0.3 }],
				messageB_opacity_out: [1, 0, { start: 0.45, end: 0.5 }],
				messageC_opacity_out: [1, 0, { start: 0.65, end: 0.7 }],
				messageD_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],
				// 사라질때는 위로(음수) 올라가면서 사라짐
				messageA_translateY_out: [0, -20, { start: 0.25, end: 0.3 }],
				messageB_translateY_out: [0, -20, { start: 0.45, end: 0.5 }],
				messageC_translateY_out: [0, -20, { start: 0.65, end: 0.7 }],
				messageD_translateY_out: [0, -20, { start: 0.85, end: 0.9 }]
			}
		},
		{
			// 1
			// 두번째는 sticky는 없음, 보통 스크롤
			type: 'normal',
			// heightNum: 5, // type normal에서는 필요 없음
			scrollHeight: 0,
			objs: {
				container: document.querySelector('#scroll-section-1'),
				content: document.querySelector('#scroll-section-1 .description')
			}
		},
		{
			// 2
			type: 'sticky',
			heightNum: 5,
			scrollHeight: 0,
			objs: {
				container: document.querySelector('#scroll-section-2'),
				messageA: document.querySelector('#scroll-section-2 .a'),
				messageB: document.querySelector('#scroll-section-2 .b'),
				messageC: document.querySelector('#scroll-section-2 .c'),
				pinB: document.querySelector('#scroll-section-2 .b .pin'),
				pinC: document.querySelector('#scroll-section-2 .c .pin'),
				canvas: document.querySelector('#video-canvas-1'),
				context: document.querySelector('#video-canvas-1').getContext('2d'),
				videoImages: []
			},
			values: {
				videoImageCount: 960,
				imageSequence: [0, 959],
				// 처음꺼는 시작부터 등장돼있기때문에 부드럽게 등장할 필요 없지만 이건 중간에 등장하기때문에 등장할때도 불투명도가 들어감!
				canvas_opacity_in: [0, 1, { start: 0, end: 0.1 }],
				canvas_opacity_out: [1, 0, { start: 0.95, end: 1 }],
				messageA_translateY_in: [20, 0, { start: 0.15, end: 0.2 }],
				messageB_translateY_in: [30, 0, { start: 0.6, end: 0.65 }],
				messageC_translateY_in: [30, 0, { start: 0.87, end: 0.92 }],
				messageA_opacity_in: [0, 1, { start: 0.25, end: 0.3 }],
				messageB_opacity_in: [0, 1, { start: 0.6, end: 0.65 }],
				messageC_opacity_in: [0, 1, { start: 0.87, end: 0.92 }],
				messageA_translateY_out: [0, -20, { start: 0.4, end: 0.45 }],
				messageB_translateY_out: [0, -20, { start: 0.68, end: 0.73 }],
				messageC_translateY_out: [0, -20, { start: 0.95, end: 1 }],
				messageA_opacity_out: [1, 0, { start: 0.4, end: 0.45 }],
				messageB_opacity_out: [1, 0, { start: 0.68, end: 0.73 }],
				messageC_opacity_out: [1, 0, { start: 0.95, end: 1 }],
				pinB_scaleY: [0.5, 1, { start: 0.6, end: 0.65 }],
				pinC_scaleY: [0.5, 1, { start: 0.87, end: 0.92 }]
			}
		},
		{
			// 3
			type: 'sticky',
			heightNum: 5,
			scrollHeight: 0,
			objs: {
				container: document.querySelector('#scroll-section-3'),
				canvasCaption: document.querySelector('.canvas-caption'),
				// 이미지 블랜드 캔버스가져옴
				canvas: document.querySelector('.image-blend-canvas'),
				context: document.querySelector('.image-blend-canvas').getContext('2d'),
				// 이미지경로
				imagesPath: [
					'./images/blend-image-1.jpg',
					'./images/blend-image-2.jpg'
				],
				// 이미지를 담을 배열
				images: []
			},
			values: {
				// 흰사각형 2개의 x좌표, 0인 이유, 지금 알 수 없기때문에 계산한 뒤 그 값을 넣어야됨
				// 종료시점도, 화면에 꽉찼을때 끝나야되기때문에 지금은 알 수 없음
				rect1X: [ 0, 0, { start: 0, end: 0 } ],
				rect2X: [ 0, 0, { start: 0, end: 0 } ],
				// 블랜딩되는 다음 이미지 -> 아래에서 계산해준 값을 넣을거다
				blendHeight: [ 0, 0, { start: 0, end: 0 } ],
				// scale이 축소되는 value
				canvas_scale: [ 0, 0, { start: 0, end: 0 } ],
				// 마지막 문단 애니메이션(시작,끝시간은 나중에 처리해줘야됨)
				canvasCaption_opacity: [ 0, 1, { start: 0, end: 0 } ],
				canvasCaption_translateY: [ 20, 0, { start: 0, end: 0 } ],
				// 여기에 나중에 Y값을 구한 뒤 첫 start값을 넣어줌!
				rectStartY: 0
			}
		}
	];
	// 이미지불러올 함수
	function setCanvasImages() {
		// 첫번째 씬이니까 [0]번째
		let imgElem;
		// 이미지개수만큼 반복문을 돌거다
		for (let i = 0; i < sceneInfo[0].values.videoImageCount; i++) {
			// 이미지 객체를 만듦 (new Image 대신 document.createElement('img')를 이용해도됨)
			imgElem = new Image();
			// 이미지 주소 순서대로 돼있음 시작번호에 i를 더함
			imgElem.src = `./video/001/IMG_${6726 + i}.JPG`;
			// 배열에 넣음
			sceneInfo[0].objs.videoImages.push(imgElem);
		}
		// 두번째 씬
		let imgElem2;
		for (let i = 0; i < sceneInfo[2].values.videoImageCount; i++) {
			imgElem2 = new Image();
			imgElem2.src = `./video/002/IMG_${7027 + i}.JPG`;
			sceneInfo[2].objs.videoImages.push(imgElem2);
		}
		// 세번째 씬
		let imgElem3;
		for (let i = 0; i < sceneInfo[3].objs.imagesPath.length; i++) {
			imgElem3 = new Image();
			imgElem3.src = sceneInfo[3].objs.imagesPath[i];
			sceneInfo[3].objs.images.push(imgElem3);
		}
	}

	function checkMenu() {
		// 문서전체에서 스크롤된 정도를 담은 변수
		// 첫번째 nav높이만큼(height가 44니까 44보다 크면 class붙임)
		if (yOffset > 44) {
			document.body.classList.add('local-nav-sticky');
		} else {
			document.body.classList.remove('local-nav-sticky');
		}
	}

	function setLayout() {
		// 각 스크롤 섹션의 높이 세팅
		// sceneIfo를 다 돌면서  네구간의 height를 다 적용해줌
		for (let i = 0; i < sceneInfo.length; i++) {
			if (sceneInfo[i].type === 'sticky') {
				// 스크롤높이를 윈도우높이(해당디바이스높이)의 heightNum만큼 곱한 수로 지정해줌(window는 생략가능)
				sceneInfo[i].scrollHeight = sceneInfo[i].heightNum * window.innerHeight;
				// normal인 것은 자기의 높이만큼만 scroll가게 만듦
			} else if (sceneInfo[i].type === 'normal')  {
				sceneInfo[i].scrollHeight = sceneInfo[i].objs.content.offsetHeight + window.innerHeight * 0.5;
			}
					// 각 섹센의 container높이를 스크롤hegith높이만큼 처리해줌
					// sticky, normal에 따라 scrolHeight가 따로 처리됨
            sceneInfo[i].objs.container.style.height = `${sceneInfo[i].scrollHeight}px`;
		}
// 새로고침을 해도 해당 scroll값의 id를 body에 넣기 위해 setLayout에도 해당 로직 적용
		yOffset = window.pageYOffset;
		// 현재 스크롤위치에 맞춰서 currentscene을 세팅해줌
		let totalScrollHeight = 0;
		for (let i = 0; i < sceneInfo.length; i++) {
			// 각 씬의 scrollheight를 다 더해줌
			totalScrollHeight += sceneInfo[i].scrollHeight;
			// totalScrollheight가 현재 scrollheight보다 크거나 같아졌을때 currentScene값을 정해주고 멈춤
			if (totalScrollHeight >= yOffset) {
				currentScene = i;
				break;
			}
		}
		document.body.setAttribute('id', `show-scene-${currentScene}`);
		// canvas의 크기를 조절! 어떠한 브라우저든 크기든 height를 100%로 맞추고 가운데 정렬을 할수있게 만들거다
		// 윈도우창높이/캔버스원래 height를 통해 비율을 구해서 그 비율대로 scale에 맞춰줌
		const heightRatio = window.innerHeight / 1080;
		// scale이 1이면 100% -> 스케일로 크기를 맞춤, 그리고 이제 가운데 정렬을 해줌
		// position의 top,left 50%로 적용하고, js에서 translate를 이용해 x:-50%,y:-50%를 적용하면 가운데 정렬이 됨 
		sceneInfo[0].objs.canvas.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`;
		sceneInfo[2].objs.canvas.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`;
	}
// 각 변화의 values(시작값과 끝값), 각 섹션마다 얼만큼의 비율로 scroll이 됐는지의 값이 필요함(현재씬에서 얼만큼 스크롤이 됐는지의 비율! 0~1, 그비율을 css값에 적용해줘야됨)
	function calcValues(values, currentYOffset) {
		let rv;
		// 현재 씬(스크롤섹션)에서 스크롤된 범위를 비율로 구하기
		const scrollHeight = sceneInfo[currentScene].scrollHeight;
		const scrollRatio = currentYOffset / scrollHeight;

		// values의 length가 3인건 시작,끝(객체)가 있단 말!
		if (values.length === 3) {
			// start ~ end 사이에 애니메이션 실행
			// 애니메이션 구간, 현재씬의 start와 end지점 구하기
			const partScrollStart = values[2].start * scrollHeight;
			const partScrollEnd = values[2].end * scrollHeight;
			// 그부분의 scrollheight를 끝지점에서 시작지점을 빼준 값
			const partScrollHeight = partScrollEnd - partScrollStart;
			// currentYOffset(현재씬에서 얼만큼 스크롤됐는지)이 start보다 크고 end보다 작을때!
			if (currentYOffset >= partScrollStart && currentYOffset <= partScrollEnd) {
				// value[1]에서 value[0]을 빼주면 처음과 끝 사이의 값을 구함 비율에 그만큼 곱해줘야 비율에 대한 값이 나오고 첫시작값을 더해줘야 그 해당 비율 만큼 시작값에서 더해짐
				// 현재 스크롤 된것에서 start만큼 빼주고 해당 부분 스크롤높이를 나눠주면 현재 파트에서 얼만큼 지났는지 비율이 나오고,
				// 그비율에서 내가 구하고자하는 값 시작과 끝의 차를 곱함(비율이니까 값을 구하기위해) 그리고 시작값을 더해줘야 해당 파트비율의 원하는 비율의 값이 됨
				rv = (currentYOffset - partScrollStart) / partScrollHeight * (values[1] - values[0]) + values[0];
				// 아직 시작전이면 rv는 초기값
			} else if (currentYOffset < partScrollStart) {
				rv = values[0];
				// 종료값보다 크면, rv는 끝값으로지정 
			} else if (currentYOffset > partScrollEnd) {
				rv = values[1];
			}
			// 시작점, 종료점이 없으면 스크롤비율만큼 값을 지정해줌!(현재씬이 시작됐을때부터 끝날때까지 적용해 줄것이기 떄문)
		} else {
			rv = scrollRatio * (values[1] - values[0]) + values[0];
		}

		return rv;
	}
// animation이 적용되는 함수
	function playAnimation() {
		// 현재씬의 각 값을 변수로 만듦
		const objs = sceneInfo[currentScene].objs;
		const values = sceneInfo[currentScene].values;
		// 현재YOffset은 yOffset값에서 이전까지 스크롤 height값을 빼주면 현재씬에서 얼만큼 scroll이 내려왔는지 알 수 있음
		const currentYOffset = yOffset - prevScrollHeight;
		// 현재씬의 scroll전체 높이
		const scrollHeight = sceneInfo[currentScene].scrollHeight;
		// 현재씬에서 얼만큼 scroll 했는지 비율
		const scrollRatio = currentYOffset / scrollHeight;
// 현재 scene만 실행되게 switch사용
		switch (currentScene) {
			case 0:
				// console.log('0 play');
				// 소수점이 아니라 정수로 index해줘야되기때문에 반올림
				// let sequence = Math.round(calcValues(values.imageSequence, currentYOffset));
				// videoImages 배열에 적혀있는 그림을, 0,0좌표부터 보여줌
				// objs.context.drawImage(objs.videoImages[sequence], 0, 0);
				// 불투명도를 calcvalues함수를 이용해서 canvas_opacity값의 불투명도만큼, 현재씬에서 얼만큼 스크롤됐는지 비율을 넣어 계산해서 넣어줌
				// 이미지는 처음부터 끝까지 다 보여줄거기 때문에 비율을 따로 안나눠도 됨!
				// 불투명도를 마지막에 끝낼때 자연스럽게 사라지게 하기 위해 적용
				objs.canvas.style.opacity = calcValues(values.canvas_opacity, currentYOffset);
				// 비율에 따라서 in과 out을 따로 적용해줌
				// 위에서 아래로 내려갈때는 in을 적용하고
				if (scrollRatio <= 0.22) {
					// in
					objs.messageA.style.opacity = calcValues(values.messageA_opacity_in, currentYOffset);
					// 3개가 필요함 x,y,z축이 필요함, 여기서 y만 조절, 3d는 하드웨어 가속이 보장됨, 그래서 3d를 많이씀!
					objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`;
					// 아래에서 위로 올라올땐 out을 적용해줘야 충돌이 일어나지 않는다
				} else {
					// out
					objs.messageA.style.opacity = calcValues(values.messageA_opacity_out, currentYOffset);
					objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_out, currentYOffset)}%, 0)`;
				}

				if (scrollRatio <= 0.42) {
					// in
					objs.messageB.style.opacity = calcValues(values.messageB_opacity_in, currentYOffset);
					objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_in, currentYOffset)}%, 0)`;
				} else {
					// out
					objs.messageB.style.opacity = calcValues(values.messageB_opacity_out, currentYOffset);
					objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_out, currentYOffset)}%, 0)`;
				}

				if (scrollRatio <= 0.62) {
					// in
					objs.messageC.style.opacity = calcValues(values.messageC_opacity_in, currentYOffset);
					objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_in, currentYOffset)}%, 0)`;
				} else {
					// out
					objs.messageC.style.opacity = calcValues(values.messageC_opacity_out, currentYOffset);
					objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_out, currentYOffset)}%, 0)`;
				}

				if (scrollRatio <= 0.82) {
					// in
					objs.messageD.style.opacity = calcValues(values.messageD_opacity_in, currentYOffset);
					objs.messageD.style.transform = `translate3d(0, ${calcValues(values.messageD_translateY_in, currentYOffset)}%, 0)`;
				} else {
					// out
					objs.messageD.style.opacity = calcValues(values.messageD_opacity_out, currentYOffset);
					objs.messageD.style.transform = `translate3d(0, ${calcValues(values.messageD_translateY_out, currentYOffset)}%, 0)`;
				}

				break;
// case1은 normal이라 control할게 없어서 뺌
			case 2:
				// console.log('2 play');
				// let sequence2 = Math.round(calcValues(values.imageSequence, currentYOffset));
				// objs.context.drawImage(objs.videoImages[sequence2], 0, 0);
				// canvas등장과 나감에 불투명도 따로 적용(0.5아니어도됨, 그냥 등장과 나감을 나눌수있을정도이면 됨)
				if (scrollRatio <= 0.5) {
					// in
					objs.canvas.style.opacity = calcValues(values.canvas_opacity_in, currentYOffset);
				} else {
					// out
					objs.canvas.style.opacity = calcValues(values.canvas_opacity_out, currentYOffset);
				}

				if (scrollRatio <= 0.32) {
					// in
					objs.messageA.style.opacity = calcValues(values.messageA_opacity_in, currentYOffset);
					objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`;
				} else {
					// out
					objs.messageA.style.opacity = calcValues(values.messageA_opacity_out, currentYOffset);
					objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_out, currentYOffset)}%, 0)`;
				}

				if (scrollRatio <= 0.67) {
					// in
					objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_in, currentYOffset)}%, 0)`;
					objs.messageB.style.opacity = calcValues(values.messageB_opacity_in, currentYOffset);
					objs.pinB.style.transform = `scaleY(${calcValues(values.pinB_scaleY, currentYOffset)})`;
				} else {
					// out
					objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_out, currentYOffset)}%, 0)`;
					objs.messageB.style.opacity = calcValues(values.messageB_opacity_out, currentYOffset);
					objs.pinB.style.transform = `scaleY(${calcValues(values.pinB_scaleY, currentYOffset)})`;
				}

				if (scrollRatio <= 0.93) {
					// in
					objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_in, currentYOffset)}%, 0)`;
					objs.messageC.style.opacity = calcValues(values.messageC_opacity_in, currentYOffset);
					objs.pinC.style.transform = `scaleY(${calcValues(values.pinC_scaleY, currentYOffset)})`;
				} else {
					// out
					objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_out, currentYOffset)}%, 0)`;
					objs.messageC.style.opacity = calcValues(values.messageC_opacity_out, currentYOffset);
					objs.pinC.style.transform = `scaleY(${calcValues(values.pinC_scaleY, currentYOffset)})`;
				}

				// currentScene 3에서 쓰는 캔버스를 미리 그려주기 시작(2번이 끝나갈떄 3번이 시작될수있게!)
				if (scrollRatio > 0.9) {
					// 변수 3번을 가져와야되는데 2번 변수와 충돌되지 않음(if안에 들어와있기 때문에)
					const objs = sceneInfo[3].objs;
					const values = sceneInfo[3].values;
					const widthRatio = window.innerWidth / objs.canvas.width;
					const heightRatio = window.innerHeight / objs.canvas.height;
					let canvasScaleRatio;

					if (widthRatio <= heightRatio) {
						// 캔버스보다 브라우저 창이 홀쭉한 경우
						canvasScaleRatio = heightRatio;
					} else {
						// 캔버스보다 브라우저 창이 납작한 경우
						canvasScaleRatio = widthRatio;
					}

					objs.canvas.style.transform = `scale(${canvasScaleRatio})`;
					objs.context.fillStyle = 'white';
					objs.context.drawImage(objs.images[0], 0, 0);
					
					// 캔버스 사이즈에 맞춰 가정한 innerWidth와 innerHeight
					// 캔버스에 적용된 scale비율로 inner 값을 따로 구함, 
					// why?? 캔버스크기 그대로 흰사각형을 만들면 실제 보이는 화면보다 캔버스가 크기때문에 잘려서 우리가 원한는대로 보이지 않을 수 있다,
					// 그렇기 떄문에 우리가 보이는 화면에 맞춘 사각형을 만들어줘야된다!
					// 창사이즈에 맞춘 캔버스 비율 Height, Width
					// 캔버스 사이즈에 맞춰 가정한 innerWidth와 innerHeight
					const recalculatedInnerWidth = document.body.offsetWidth / canvasScaleRatio;
					const recalculatedInnerHeight = window.innerHeight / canvasScaleRatio;
					// 하얀사각형 폭, 창사이즈에 맞춘 캔버스 비율에 15%(디자인에따라 바꾸면됨)
					const whiteRectWidth = recalculatedInnerWidth * 0.15;
					// 전체에서 안쪽화면을 뺀 후 절반(높이에 맞췄기 때문에 캔버스가 화면보다 더 커서 나간 캔버스의 한쪽크기(왼쪽,오른쪽)를 구할 수 있다)
					// 거기서 부터 그려야된다는말!(그래야 캔버스크기에서 화면에 보이는 곳부터 사각형이 그려짐)
					values.rect1X[0] = (objs.canvas.width - recalculatedInnerWidth) / 2;
					// 끝의 x좌표는 결국 흰사각형이 화면밖으로 나가야됨, 그러니까 시작하는 x좌표에서 흰사각형width만큼 빼주면됨
					values.rect1X[1] = values.rect1X[0] - whiteRectWidth;
					// 여긴 화면 오른쪽에 사각형을 만들어야되기때문에 화면의 시작부터 화면크기만큼 더한뒤(오른쪽 끝의좌표가 나옴) 여기서 사각형만큼 빼주면 거기서 부터 시작!
					values.rect2X[0] = values.rect1X[0] + recalculatedInnerWidth - whiteRectWidth;
					// 시작부터 사각형만큼 더한만큼 이동해야됨!
					values.rect2X[1] = values.rect2X[0] + whiteRectWidth;

					// 그림이 올라가면서 옆으로 커지는 듯한 느낌이 들게하는 방법중,
					// 1. 흰색 div두개를 좌우에 만들고 스크롤이 올라갈때 옆으로 벌리게 할 수도 있고(애플은 이방법 이용)
					// 2. canvas로 직접 그려서 표현할 수도있다
					// 좌우 흰색 박스 그리기(2번)
					// fillRect는 사각형을 그리는 메서드 fillRect(x좌표, y좌표,width,height)
					// parseInt(정수처리)
					// 높이는 캔버스크기만큼 꽉채움
					// 초기값으로 설정
					objs.context.fillRect(
						parseInt(values.rect1X[0]),
						0,
						parseInt(whiteRectWidth),
						objs.canvas.height
					);
					objs.context.fillRect(
						parseInt(values.rect2X[0]),
						0,
						parseInt(whiteRectWidth),
						objs.canvas.height
					);
				}

				break;

			case 3:
				// console.log('3 play');
				// step을 나눔!(구조가 복잡하니까 각 동작별로 나눈다)
				let step = 0;
				// (어떤브라우저든)가로/세로 모두 꽉 차게 하기 위해 여기서 세팅(계산 필요)
				// 너비비율
				const widthRatio = window.innerWidth / objs.canvas.width;
				// 높이비율
				const heightRatio = window.innerHeight / objs.canvas.height;
				let canvasScaleRatio;
				// 브라우저 비율에따라 캔버스비율 조절
				if (widthRatio <= heightRatio) {
					// 캔버스보다 브라우저 창이 홀쭉한 경우
					canvasScaleRatio = heightRatio;
				} else {
					// 캔버스보다 브라우저 창이 납작한 경우
					canvasScaleRatio = widthRatio;
				}
				// 캔버스 scale을 조절
				objs.canvas.style.transform = `scale(${canvasScaleRatio})`;
				// 사각형 색을 white로 지정
				objs.context.fillStyle = 'white';
				// 첫번째이미지를 캔버스에 먼저 그려줌
				objs.context.drawImage(objs.images[0], 0, 0);

				// 캔버스 사이즈에 맞춰 가정한 innerWidth와 innerHeight
				// 캔버스에 적용된 scale비율로 inner 값을 따로 구함, 
				// why?? 캔버스크기 그대로 흰사각형을 만들면 실제 보이는 화면보다 캔버스가 크기때문에 잘려서 우리가 원한는대로 보이지 않을 수 있다,
				// 그렇기 떄문에 우리가 보이는 화면에 맞춘 사각형을 만들어줘야된다!
				// 창사이즈에 맞춘 캔버스 비율 Height, Width
				// width를 window.innerWidth로 계산을 하면 스크롤바도 포함한 width라서 계산에 오차가 생긴다. 그래서 body.offsetWidth로 계산!
				const recalculatedInnerWidth = document.body.offsetWidth / canvasScaleRatio;
				const recalculatedInnerHeight = window.innerHeight / canvasScaleRatio;
				// rectStartY값이 아직 지정이 안돼있다면 -> 지정해줌
				if (!values.rectStartY) {
					// getBoundClientRect : 화면상에 보이는 object에 크기와 위치를 가져오는 메서드
					// 화면상에 보이는 캔버스의 top위치를 가져옴, 하지만 이건 스크롤할때마다 값이 바뀌어서 기준으로 사용할 수 없음 -> 시작시점에 한번만 가져옴!
					// 이렇게 해서 기준으로 해도되지만 문제점이 있다! 만약 스크롤 속도에 따라 값이 달라짐!!(정확성이 떨어진다)
					// values.rectStartY = objs.canvas.getBoundingClientRect().top;
					// offsetTop이용, canvas의 y위치를 가져옴(getBoundingClientRect보다 복잡함)
					// 스크롤을 빠르게 하나, 느리게하나 같은 값(고정값이라) 근데 기준이 스크롤 처음부터임
					// 3번 섹션이 시작됐을때 top이 얼만큼 떨어져있는지 구하고싶다 
					// offsetTop은 기준을 바꿀 수 있다
					// -> 부모의 position을 static이 아닌 값, 보통 relative로 만들어서 기준을 처음이아니라 section시작으로 되게 한다.
					// why? relative는 컨테이너 자체의 위치는 영향을 받지 않지만 안에있는 자식들의 기준이 나(relative인부모)로 된다
					// 이렇게 맞춰도 top높이가 맞지 않다 why? 캔버스를 tranlate scale을 이용해서 줄였기 때문
					// translate를 이용해 위치이동이나 크기를 줄여도 canvas 자체의 크기는 변하지 않음, 그래서 기본적인 canvas가 차지하는 공간은 시각적으로만 변한것이기 때문에 값이 화면상 보이는 값과 다르다!
					// 원래 canvas값의 offsetTop이란 말!
					// scale조정한 값만큼 또 적용해줘야됨
					// 원래 canvas높이에 줄어든canvas높이를 뺀 값에서 /2(위쪽만 구할거기떄문)그만큼 더해주면 됨!
					values.rectStartY = objs.canvas.offsetTop + (objs.canvas.height - objs.canvas.height * canvasScaleRatio) / 2;
					// 애니메이션 시작과 종료시점 구하기
					// 윈도우(화면) 높이의 절반부터 시작하게 만듦
					values.rect1X[2].start = (window.innerHeight / 2) / scrollHeight;
					values.rect2X[2].start = (window.innerHeight / 2) / scrollHeight;
					// 전체 스크롤높이에 rectStartY를 나눈값 만큼 진행됨(rectStartY값만큼 올라가면 끝남)
					values.rect1X[2].end = values.rectStartY / scrollHeight;
					values.rect2X[2].end = values.rectStartY / scrollHeight;
				}
				// 하얀사각형 폭, 창사이즈에 맞춘 캔버스 비율에 15%(디자인에따라 바꾸면됨)
				const whiteRectWidth = recalculatedInnerWidth * 0.15;
				// 0은 시작값, 1은 끝값
				values.rect1X[0] = (objs.canvas.width - recalculatedInnerWidth) / 2;
				values.rect1X[1] = values.rect1X[0] - whiteRectWidth;
				values.rect2X[0] = values.rect1X[0] + recalculatedInnerWidth - whiteRectWidth;
				values.rect2X[1] = values.rect2X[0] + whiteRectWidth;

				// 그림이 올라가면서 옆으로 커지는 듯한 느낌이 들게하는 방법중,
				// 1. 흰색 div두개를 좌우에 만들고 스크롤이 올라갈때 옆으로 벌리게 할 수도 있고(애플은 이방법 이용)
				// 2. canvas로 직접 그려서 표현할 수도있다
				// 좌우 흰색 박스 그리기(2번)
				// fillRect는 사각형을 그리는 메서드
				// calcValues를 사용해서 사각형 움직임
				objs.context.fillRect(
					parseInt(calcValues(values.rect1X, currentYOffset)),
					0,
					parseInt(whiteRectWidth),
					objs.canvas.height
				);
				objs.context.fillRect(
					parseInt(calcValues(values.rect2X, currentYOffset)),
					0,
					parseInt(whiteRectWidth),
					objs.canvas.height
				);
				// 스크롤 ratio가 cavas가 상단에 닿기전까진 step이 1
				if (scrollRatio < values.rect1X[2].end) {
					// console.log('캔버스 닿기 전');
					step = 1;
					// 캔버스에 닿기전 sticky클래스를 제거함
					objs.canvas.classList.remove('sticky');
				} else {
					// console.log('캔버스 닿은 후');
					step = 2;
					// 이미지 블렌드
					// values.blendHeight: [ 0, 0, { start: 0, end: 0 } ]
					//처음,끝,2(start,end) 초기값설정
					values.blendHeight[0] = 0;
					// 최종값은 canvas의 높이까지
					values.blendHeight[1] = objs.canvas.height;
					// 만든 사각형의 애니메이션이 끝날때 시작함
					values.blendHeight[2].start = values.rect1X[2].end;
					// 끝(end타이밍 -> 속도) 내가 정하면 됨 -> 20%정도 스크롤할때까지만!
					values.blendHeight[2].end = values.blendHeight[2].start + 0.2;
					// blendHeight는 위에서 정한 값으로 calcValues를 이용해 값을 구함(계속변함, 이걸 이용해 drawimage에 적용)
					const blendHeight = calcValues(values.blendHeight, currentYOffset);
					// 블랜드할 이미지를 그림, 
					// drawImage(image,sx,sy,sWidth,sHeight,dx,dy,dWidth,dHeight) 
					// s는 source(원래우리가 그릴 이미지), d(destination,캔버스에 실제로 그리는 이미지)
					// s는 원래 이미지에서 위치할 부분, d는 캔버스에 위치할 부분
					// 2번째 이미지를 sy(canvas높이에서 blendHeight만큼 뺀 값이 y좌표), sWidth는 전체, sHegit는 blendHeight만큼,
					// d는 s랑 같음! 왜냐하면 canvas크기랑 이미지 크기를 같게 만들었기 때문!
					// 여기서 blendHeight는 위의 계산한 결과값으로 들어옴
					objs.context.drawImage(objs.images[1],
						0, objs.canvas.height - blendHeight, objs.canvas.width, blendHeight,
						0, objs.canvas.height - blendHeight, objs.canvas.width, blendHeight
					);
					// class에 sticky를 추가
					objs.canvas.classList.add('sticky');
					// top을 offsetTop을 구했을때처럼 바꾼만큼 뺀 px을 적용해줌
					objs.canvas.style.top = `${-(objs.canvas.height - objs.canvas.height * canvasScaleRatio) / 2}px`;

					// scrollRatio가 blend가 끝난 시점에 scale축소가 시작됨
					if (scrollRatio > values.blendHeight[2].end) {
						// 캔버스scale 축소 시작은 원래 상태
						values.canvas_scale[0] = canvasScaleRatio;
						// 최종값은 얼마만큼 줄일건지, 브라우저의 폭을 기준으로함(브라우저가 달라져도 되게)
						// 분수니까 분모의 값을 증가시켜 결과값을 작게 만듦(내가 원하는 크기만큼)
						values.canvas_scale[1] = document.body.offsetWidth / (1.5 * objs.canvas.width);
						// 그전 애니메이션이 끝났을때 시작
						values.canvas_scale[2].start = values.blendHeight[2].end;
						// 끝도 내가 원하는 만큼까지만
						values.canvas_scale[2].end = values.canvas_scale[2].start + 0.2;
						// canvas의 scale을 조절해줌
						objs.canvas.style.transform = `scale(${calcValues(values.canvas_scale, currentYOffset)})`;
						// static에서 fixed로 다시 바꿀때(아래에서 위로 다시 올라올때) marginTop을 다시 0으로 바꿔줘야됨
						objs.canvas.style.marginTop = 0;
					}
					// scale축소 애니매이션이 끝났고,초기값이 0이기때문에 0보다 클때 stickyclass를 제거함,
					if (scrollRatio > values.canvas_scale[2].end
						&& values.canvas_scale[2].end > 0) {
						objs.canvas.classList.remove('sticky');
						// fixed인채로 이미 스크롤을 많이 내려버렸기 때문에 static이 됐을때 위에 위치하게 됨, 그래서 margintop 줌
						// 이미지가 블랜드되고, scale축소 시간을 합하면 (0.2+0.2) -> 0.4가 된다. 그만큼 margintop을 줌
						objs.canvas.style.marginTop = `${scrollHeight * 0.4}px`;

						// 마지막문단 애니메이션 처리
						// 캔버스축소가 끝날때 시작
						values.canvasCaption_opacity[2].start = values.canvas_scale[2].end;
						// 10%만큼 스크롤될동안
						values.canvasCaption_opacity[2].end = values.canvasCaption_opacity[2].start + 0.1;
						values.canvasCaption_translateY[2].start = values.canvasCaption_opacity[2].start;
						values.canvasCaption_translateY[2].end = values.canvasCaption_opacity[2].end;
						objs.canvasCaption.style.opacity = calcValues(values.canvasCaption_opacity, currentYOffset);
						objs.canvasCaption.style.transform = `translate3d(0, ${calcValues(values.canvasCaption_translateY, currentYOffset)}%, 0)`;
					} else {
						// 
						objs.canvasCaption.style.opacity = values.canvasCaption_opacity[0];
					}
				}

				break;
		}
	}

	function scrollLoop() {
		// 새로운 scene이 시작된 순간, 초기화(false)
		enterNewScene = false;
		// 0으로 초기화를 해줘야됨, 그래야 값이 누적안되고 계속 현재 scrollheight값으로 찍힘
		prevScrollHeight = 0;
// 현재 scrollhegit값을 구함, 현재 내 위치기준으로 더 위에있는 scrollheight값을 다 더함
		for (let i = 0; i < currentScene; i++) {
			prevScrollHeight += sceneInfo[i].scrollHeight;
		}
		// yOffset이 아니라 delayedYOffset을 기준으로!(비디오 감속처리를 위해)
		if (delayedYOffset < prevScrollHeight + sceneInfo[currentScene].scrollHeight) {
			// scrolleffect가 필요한 범위내에서는 다시 remove로 지워서 보이게 만듦
			document.body.classList.remove('scroll-effect-end');
		}

		if (delayedYOffset > prevScrollHeight + sceneInfo[currentScene].scrollHeight) {
			// 바뀌는 순간에 true로 바꿈
			enterNewScene = true;
			if (currentScene === sceneInfo.length - 1) {
				// 스크롤 효과가 모두 끝나고, 아래 일반 콘텐츠 영역에서는 sticky-elem들을 모두 안보이도록 지정한 class를 추가함
				document.body.classList.add('scroll-effect-end');
			}
			// currentScene이 마지막 index보다 하나 작을떄까지만 더해지게함
			if (currentScene < sceneInfo.length - 1) {
				currentScene++;
			}
			// currentScene에 맞춰서 해당 스크롤섹션의 내용의 id값으로 body에 id값으로 들어감 -> display:none에서 block으로 바뀜
			document.body.setAttribute('id', `show-scene-${currentScene}`);
		}

		if (delayedYOffset < prevScrollHeight) {
			enterNewScene = true;
			// 브라우저 바운스 효과로 인해 마이너스가 되는 것을 방지(모바일)
			if (currentScene === 0) return;
			currentScene--;
			document.body.setAttribute('id', `show-scene-${currentScene}`);
		}
// enterNEwScene(씬이 바뀌는 순간)이 true라면 바로 return -> 이렇게 처리하면 처음씬이 바뀌는 순간 음수값이 나올때 한턴 playAnimation이 걸러짐(계산의 오차를 해결)
// 오동작을 일으킬 원인이 되는 것을 사전에 막아줌
		if (enterNewScene) return;

		playAnimation();
	}
	// 부드러운 감속을 위한 함수
	function loop() {
		// pageyOffset => yOffset
		delayedYOffset = delayedYOffset + (yOffset - delayedYOffset) * acc;
		// 씬이 바뀌는 순간에만 오류가 나니까 씬이 바뀌는 순간은 적용안되게 함
		if (!enterNewScene) {
			// 현재 씬이 0이거나 2일때만 그려내게함
			if (currentScene === 0 || currentScene === 2) {
				// 가속도가 적용된 delayedYoffset을 pageyoffset대신 써야됨
				const currentYOffset = delayedYOffset - prevScrollHeight;
				// 각 씬의 value와 objs를 가져옴
				const objs = sceneInfo[currentScene].objs;
				const values = sceneInfo[currentScene].values;
				// 이미지를 부드럽게 그려내기 위해 여기에 적용
				let sequence = Math.round(calcValues(values.imageSequence, currentYOffset));
				// 이미지가 존재할때만 보여지게함
				if (objs.videoImages[sequence]) {
					objs.context.drawImage(objs.videoImages[sequence], 0, 0);
				}
			}
		}

        // 일부 기기에서 페이지 끝으로 고속 이동하면 body id가 제대로 인식 안되는 경우를 해결
        // 페이지 맨 위로 갈 경우: scrollLoop와 첫 scene의 기본 캔버스 그리기 수행
        if (delayedYOffset < 1) {
            scrollLoop();
            sceneInfo[0].objs.canvas.style.opacity = 1;
            sceneInfo[0].objs.context.drawImage(sceneInfo[0].objs.videoImages[0], 0, 0);
        }
        // 페이지 맨 아래로 갈 경우: 마지막 섹션은 스크롤 계산으로 위치 및 크기를 결정해야할 요소들이 많아서 1픽셀을 움직여주는 것으로 해결
        if ((document.body.offsetHeight - window.innerHeight) - delayedYOffset < 1) {
            let tempYOffset = yOffset;
            scrollTo(0, tempYOffset - 1);
        }

		rafId = requestAnimationFrame(loop);

		if (Math.abs(yOffset - delayedYOffset) < 1) {
			cancelAnimationFrame(rafId);
			rafState = false;
		}
	}
// 새로고침되면 setLayout이 실행됨
// 'load'vs 'DOMContentLoaded', 둘차이는 load는 웹페이지 이미지,리소스 등 모두 로딩되고나서 실행, DOM은 html객체 돔구조가 로드되면 실행, 보통 이걸 많이 쓰지만 우리는 현재 이미지와 같은것이 다 로드되고 실행돼야 의미가 있어서 load사용
	window.addEventListener('load', () => {
		setLayout(); // 중간에 새로고침 시, 콘텐츠 양에 따라 높이 계산에 오차가 발생하는 경우를 방지하기 위해 before-load 클래스 제거 전에도 확실하게 높이를 세팅하도록 한번 더 실행
	    document.body.classList.remove('before-load');
				setLayout();
				// 처음 새로고침했을때 캔버스에 제일 첫 사진이 보이게 가져옴
        sceneInfo[0].objs.context.drawImage(sceneInfo[0].objs.videoImages[0], 0, 0);

		// 중간에서 새로고침 했을 경우 자동 스크롤로 제대로 그려주기
		// 현재위치를 저장할 변수
				let tempYOffset = yOffset;
				// 스크롤이 몇번됐는지 셀 변수
				let tempScrollCount = 0;
				// 제일 처음일때는 일어나지않게함(스크롤이되면 안되기때문)
        if (tempYOffset > 0) {
					// settimeout은 한번잠깐 지연, setInterval은 계속 반복시킴
            let siId = setInterval(() => {
							// 현재위치로 스크롤을 보냄
								scrollTo(0, tempYOffset);
								// 스크롤을 5px씩 20번반복할거다
                tempYOffset += 5;
								// 20까지만 할거니까(0.02초) 20넘으면 멈춰라
                if (tempScrollCount > 20) {
                    clearInterval(siId);
								}
								// temp가 몇번반복됐는지 세어줌
                tempScrollCount++;
            }, 20);
				}
// 모든 과정은 load가 된 후 실행돼야 되니까 load 안에 넣어줌
// 스크롤시에 안에 함수가 실행됨
        window.addEventListener('scroll', () => {
					// 스크롤이 일어날 때 yOffset에 pageYOffset값을 할당해줌
						yOffset = window.pageYOffset;
						// 그 뒤에 scrollLoop함수가 실행됨
            scrollLoop();
  			checkMenu();
				// scroll이 일어났고, requestAnimation상태가 꺼져있으면 다시 실행시킴
  			if (!rafState) {
  				rafId = requestAnimationFrame(loop);
  				rafState = true;
  			}
  		});
// 윈도우 사이즈를 줄이면 다시 높이 조정(setlayout실행)
  		window.addEventListener('resize', () => {
				// innerWidth가 900(폰들이 요즘 900까지 됨)보다 클때만 
  			if (window.innerWidth > 900) {
					// reload를 시킴(새로고침)
				window.location.reload();
			}
  		});
			// orientationchange는 모바일 가로 세로 방향 바꾸는 이벤트!가 일어나면 함수가 실행되게 처리
  		window.addEventListener('orientationchange', () => {
			// 로드됐을때 자동으로 살짝 스크롤해줌(스크롤이벤트가 일어나야 보여지는 화면이 있기 떄문)
			// scrollTo(x,y)
			// 스크롤자체를 그냥 위로 올려줌
			scrollTo(0, 0);
			// orientation했을때 camvas크기가 제대로 안잡혀서 한템포 늦춰서 실행되게함
			setTimeout(() => {
				// 다시 reload시킴
				window.location.reload();
			}, 500);
  		});
			// 로딩이 끝난 뒤 로딩 자체를 없애야되는데 부드럽게 없어지게 하기 위해 transitionend이벤트(transition이 끝나면 없어지게 함)이용
  		document.querySelector('.loading').addEventListener('transitionend', (e) => {
				// event의 타겟을 없앰
				// (참고로, 화살표 함수를 사용했기 때문에 this는 사용할 수 없다, 화살표 함수 안에서의 this는 전역객체를 가리킴(?????))
  			document.body.removeChild(e.currentTarget);
  		});

	});

	setCanvasImages();

})();
