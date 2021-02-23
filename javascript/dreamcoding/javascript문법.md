# Javascript

> [Javascript 공식문서](https://www.ecma-international.org/)
>
> [Javascript MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript)
>
> - 바닐라js로 개발을 할때는 코드 제일위에 `'use strict';`를 적어줌 그러면 비상식적인 코드를 적을시에 오류가 뜸 -> 예를들어 아래코드를 봄
>
> ```js
> // 이것만 적으면 오류남
> 'use strict';
> a = 6;
> 
> // a를 선언해줘야됨
> let a;
> a = 6;
> ```

- html에 js를 포함할때 어떤 순서대로 사용자에게 보여지는가?

1. html `<head>`태그안에 `<script src="main.js"></script>`가 포함

- 위에서 부터 읽다가 js를 먼저 import하고 `body태그를 불러옴`
- 단점 : js파일이 많이 클때 js를 불러올때까지 아래가 불러와지지 않아서 로딩이 많이 걸림

1-2.  html `<head>`태그안에 `<script async src="main.js"></script>`가 포함

- `async`은 `boolean`값이기 때문에 선언만 하면 true로 async옵션이 적용됨
- 위에서부터 parsing하다가 `asyn`때문에 fetching시작하고 html은 계속 parsing하다가  js가 fetching이 끝나면 잠시 parsing을 멈추고 js 실행한다음 다시 parsing시작
- 여러개의 js가 `async`로 돼있으면 여러개 중 fetching이 끝난 js가 먼저 실행됨! 그때 html parsing은 잠시 멈춤
- 장점:  body끝에 script를 쓰는것보다 parsing이 병렬적으로 일어나기 때문에 다운로드 받는 시간을 절약할 수 있다
- 단점 : js가 html이 parsing되기 전에 실행되기 때문에 js에서 dom을 조작하는 `queryselector`같은게 있으면 아직 dom 요소가 다 parsing 되지 않아서 적용되지 않을 수 있음, 실행될때 잠시 parsing이 멈추기 때문에 사용자가 페이지를 볼때 시간이 더 걸릴 수 있음 

1-3.  html `<head>`태그안에 `<script defer src="main.js"></script>`가 포함

- `defer`는 위에서부터 parsing하다가 fetching받으라고 명령한 뒤, 끝까지 parsing하고 끝났을때 실행시킴
- 여러개의 js가`defer`로 돼있으면 fetching은 html이 parsing되면서 다 되고, parsing이 완료됐을때 위에서부터 적혀있는 순서대로 js가 실행됨

2. `<body>`태그 제일끝에 `<script src="main.js"></script>`가 포함

- 페이지가 준비된다음에 js를 fetching하고 실행함
- 단점 : 사용자가 기본적인 html컨텐츠를 빨리볼수는 있지만 js에 의존적인 페이지일 경우 사용자가 정상적인 페이지를 보기 힘들다



## 입력, 연산, 출력

> 변수 선언은 `let`(mutable) - read & write, `const`(immutable) - read only 만 사용
>
> 대부분 선언 -> 할당 (`var`사용하지마라! 호이스팅때문.. 어디에 선언했냐에 관계없이 끌어올려 할당 -> 선언이 가능해짐, 그리고 block scope이 없음! )
>
> `const` 선언과 동시에 할당하고 값이 변경되지 않음! -> 보안상, 동시에 변수에 접근해서 할당하지 못하게함  **주로 const이용**

- Number

```js
// 숫자는 Number[over (-2**53) ~ 2**53]까지 표현가능
// 하지만 넘는 숫자 끝에 'n'만 추가하면 'bigint'타입이 된다(현재 크롬, 파이어폭스만 지원됨)
const infinity = 1/0;
const negativeInfinity = -1/0;
const nAn = 'not a number' / 2;
console.log(infinity); // Infinity
console.log(negativeInfinity); // -Infinity
console.log(nAn); // NaN
```

- boolean
  - false : 0, null, undefined, NaN, ''
  - true : any other, value

- Symbol
  - 주어진 string에 관계없이 고유한 식별자를 주고싶을 때

```js
// symbol, create unique identifiers for objects
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // false
const gSymbol1 = Symbol.for('id');
const gSymbol2 = Symbol.for('id');
console.log(gSymbol1 === gSymbol2); // true

// symbol은 .description을 통해 string으로 변환해서 출력해야됨
console.log(`value : ${symbol1.description}, type : ${typeof symbol1}`)
//value : id, type : symbol
```

- Dynamic typing

```js
let text = 'hello';
console.log(`value:${text}, type : ${typeof text}`); // value:hello,type : string
text = 1;
console.log(`value:${text}, type : ${typeof text}`); // value:1,type : number
text = '7' + 5;
console.log(`value:${text}, type : ${typeof text}`); // value:75,type : string
text = '8' / '2';
console.log(`value:${text}, type : ${typeof text}`); // value:4,type : number
console.log(text.charAt(0)); // TypeError -> text는 number이기 때문에!
```



## 연산, 반복문

- operator.js

``` js
// 1. String concatenation
console.log('my' + 'cat'); //my cat
console.log('1' + 2); // 12
console.log(`string literals: 1 + 2 = ${1 + 2}`); // string literals: 1 + 2 = 3
// 줄바꿈이나 안에 ""를 쓰고 싶을때 백슬래쉬사용 '\" -> "' \n-> 줄바꿈, \t-> tab

// 2. Numeric operatiors
console.log(1+1); // add 2
console.log(1-1); // substract 0
console.log(1/1); // divide 1
console.log(1*1); // multiply 1
console.log(1%1); // remainder 1
console.log(2**3); // exponentiation 8

// 3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter; // counter = counter + 1;preIncrement = counter;
console.log(`preIncrement: ${postIncrement}, counter: ${counter}`); // preIncrement: 3, counter:3
//++ or --가 앞에 붙으면 숫자에 변화가 생기고 할당, 뒤에 붙으면 숫자를 할당하고 변화시킴

// 4. Assignment operators
let x = 3;
let y = 6;
x += y; // x = x+y;
x -= y;
x *= y;
x /= y;

// 5. Comparison operators <, >, <=, >=
console.log(10 <6); //less than

// 6. logical operators : ||(or), &&(and), !(not)
const value1 = false;
const value2 = 4 < 2;
// ||(or)은 true가 앞에 나오면 멈춤, 그래서 복잡한 연산은 뒤에 오게함(효율적)
// &&(and)는 앞에가 false(null)가 나오면 멈춤, 그래서 이것도 복잡한 연산은 뒤에오게함

// 7. equality
// == loose equality '5' == 5
// === strict equlity(type까지 같아야됨) '5' !== 5, 5===5

// object equality by reference
const iris1 = {name:'iris'};
const iris2 = {name:'iris'};
const iris3 = iris1;
console.log(iris1 == iris2); // false (다른 reference이기 때문)
console.log(iris1 === iris2); // false (다른 reference이기 때문)
console.log(iris1 === iris3); // true

// quiz
console.log(0 == false); // true
console.log(0 === false); // false
console.log('' == false); // true
console.log('' === false); //false
console.log(null == undefinded); // true
console.log(nul === undefinded); // false

// 8. if
const name ='iris';
if (name === 'iris') {
    console.log('Welecome,Iris');
} else if (name === 'coder') {
    console.log('You are amazing coder');
} else {
    console.log('unknown');
}

// 9. ? 삼항연산자
// condition ? value1 : value2;
console.log(name === 'iris' ? 'yes':'no'); //yes

// 10 switch
const browser = 'IE';
switch (browser) {
    case 'IE':
        console.log('go away!');
        break;
    // 조건결과 같으면 case연달아 쓰면 됨!
    case 'Chrome':
    case 'Firefox':
        console.log('love you!');
        break;
    default:
        console.log('same all!');
        break;       
}

// 11. Loop
let i = 3;
while (i > 0) {
    console.log(`while ${i}`);
    i--;
}
// while: 3; while: 2; while: 1;
// do while -> do안의 조건이 끝나고, while의 조건이 맞다면 while실행
do {
  console.log(`do while" ${i}`);
    i-- ;
} while (i>0);

// for loop(begin; condition; step)
for (i = 3; i > 0; i--) {
    console.log(`for ${i}`);
}
// break는 loop를 완전히 끝냄 continue는 지금꺼만 스킵하고 다음 스텝으로 넘어감
```



## Functions

> objects의 일종

```js
// default parameters
// from이 파라미터로 전달되지 않으면 default값으로 unknown이 들어있음
function showMessage(message, from = 'unknown') {
    console.lpg(`${message} by ${from}`);
}
showMessage('Hi!');

// ... rest parameters -> 배열형태로 전달됨
function printAll(...args) { 
	for (let i = 0; i < args.length, i++) {
        console.log(args[i]);
    }
}
printAll('dream','coding','iris');

// for of : args의 모든값들이 arg로 출력됨
for (const arg of args) {
    console.log(arg);
}
// ===> forEach
args.forEach((arg) => console.log(arg));

// IIFE : Immediately Invoked Function Expression 즉시실행함수
(function hello() {
    console.log('IIFE');
})();
```



