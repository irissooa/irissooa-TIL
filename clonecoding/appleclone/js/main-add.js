// "main.js 적용 내용" 강의에서 추가된 부분을 따로 정리해 놓은 파일입니다.
// 아래 내용을 작성하고 계신 main.js의 해당 부분에 붙여 넣으시면 됩니다.



// sceneInfo 추가내용 적용 후
const sceneInfo = [
    {
        // 0
        type: 'sticky',
        heightNum: 5, // 브라우저 높이의 5배로 scrollHeight 세팅
        scrollHeight: 0,
        objs: {
            container: document.querySelector('#scroll-section-0'),
            messageA: document.querySelector('#scroll-section-0 .main-message.a'),
            messageB: document.querySelector('#scroll-section-0 .main-message.b'),
            messageC: document.querySelector('#scroll-section-0 .main-message.c'),
            messageD: document.querySelector('#scroll-section-0 .main-message.d')
        },
        values: {
            messageA_opacity_in: [0, 1, { start: 0.1, end: 0.2 }],
            messageB_opacity_in: [0, 1, { start: 0.3, end: 0.4 }],
            messageC_opacity_in: [0, 1, { start: 0.5, end: 0.6 }],
            messageD_opacity_in: [0, 1, { start: 0.7, end: 0.8 }],
            messageA_translateY_in: [20, 0, { start: 0.1, end: 0.2 }],
            messageB_translateY_in: [20, 0, { start: 0.3, end: 0.4 }],
            messageC_translateY_in: [20, 0, { start: 0.5, end: 0.6 }],
            messageD_translateY_in: [20, 0, { start: 0.7, end: 0.8 }],
            messageA_opacity_out: [1, 0, { start: 0.25, end: 0.3 }],
            messageB_opacity_out: [1, 0, { start: 0.45, end: 0.5 }],
            messageC_opacity_out: [1, 0, { start: 0.65, end: 0.7 }],
            messageD_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],
            messageA_translateY_out: [0, -20, { start: 0.25, end: 0.3 }],
            messageB_translateY_out: [0, -20, { start: 0.45, end: 0.5 }],
            messageC_translateY_out: [0, -20, { start: 0.65, end: 0.7 }],
            messageD_translateY_out: [0, -20, { start: 0.85, end: 0.9 }]
        }
    },
    {
        // 1
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
            pinC: document.querySelector('#scroll-section-2 .c .pin')
        },
        values: {
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
            canvasCaption: document.querySelector('.canvas-caption')
        },
        values: {

        }
    }
];



// playAnimation 추가내용 적용 후
function playAnimation() {
    const objs = sceneInfo[currentScene].objs;
    const values = sceneInfo[currentScene].values;
    const currentYOffset = yOffset - prevScrollHeight;
    const scrollHeight = sceneInfo[currentScene].scrollHeight;
    const scrollRatio = currentYOffset / scrollHeight;

    switch (currentScene) {
        case 0:
            // console.log('0 play');
            if (scrollRatio <= 0.22) {
                // in
                objs.messageA.style.opacity = calcValues(values.messageA_opacity_in, currentYOffset);
                objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`;
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

        case 2:
            // console.log('2 play');
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

            break;

        case 3:
            // console.log('3 play');
            break;
    }
}
