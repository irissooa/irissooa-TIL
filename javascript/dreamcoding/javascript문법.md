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



## class or object

- class는 템플릿! 데이터는 없음 틀만 있다
- object는 class를 이용해서 data를 넣어서 만드는것, 클래스의 인스턴스

### class

```js
'use strict';
// class: template
// object : instance of a class

// 1. class 선언
class Person {
    //constructor
    constructor(name,age) {
        //fields
        this.name = name;
        this.age = age;
    }
    
    //methods
    speak() {
        console.log(`${this.name}: hello!`);
    }
}

const iris = new Person('iris', 20);
console.log(iris.name); // iris
console.log(iris.age); // 20
iris.speak(); // iris: hello!


// 2. Getter and setters
class User {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
    // getter가 정의된 순간 위의 this.age는 메모리에(constructor) age가 아니라 getter를 호출한다. 
    get age() {
        // return this.age;
        return this._age;
    }
    // set은 값을 설정하기 때문에 value를 받아와야됨
    // setters를 정의하는 순간 constuctor의 `=age`는 메모리의 age를 할당하는 것이 아니라 set age(value)를 호출하게됨! setter에 전달된 value를 this.age에 할당! 
    set age(value) {
        // this.age = value; // 그래서 이렇게 적어두면 this.age= value에서 `=value`는 setter를 계속 반복적으로 호출해서 Maximum call stack size exceeded에러가 발생! 그래서 this.age가 아니라 다른 변수 이름을 줘야됨, 보통 age앞에 '_'를 붙임
        // 조건 1번방법
        if (value < 0) {
            throw Error('age can not be negative');
        }
        // 조건 2번방법
        this._age = value < 0 ? 0 : value;
    }
}
// 사용자가 실수로 나이를 -1로 함 -> 사용자가 class를 잘못사용해도 좀더 방어적으로 만들어주는것이 getter와 setters!
const user1 = new User('Steve','Job',-1);
console.log(user1.age); // 0



// 3. Fields(Public & Private) -> 현재 너무 새로나온 문법이라 최신 브라우저에서는 적용이 안됨(사파리..)

calss Experiment {
    publicField = 2;
    // #(해시기호) : class 내부에서만 값이 보여지고 접근되고 값이 변경가능
    #privateField = 0;
}
const experiment = new Experiment();
console.log(experiment.publicField); // 2
console.log(experiment.privateField); // undefined

// 4. Static : object에 관계없이 class에 공통적으로 쓸수 있는 값, 메소드(메모리 사용을 줄여줌)
class Article {
    static publisher = 'Dream Coding';
	constructor(articleNumber) {
        this.articleNumber = articleNumber;
    }
	static printPublisher() {
        console.log(Article.publisher);
    }
}
const article1 = new Article(1);
const article2 = new Article(2);
console.log(article.publisher); // undefinded -> static은 object자체에 지정된 값이 아니라 class에 지정된 값
console.log(Article.publisher); // Dream Coding
// static함수를 호출할 때도 Class명을 이용해 호출
Article.printPublisher(); // Dream Coding

// 5. Inheritance 상속, 다양성
class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }
    draw() {
        console.log(`drawing ${this.color} color!`);
    }
    
    getArea() {
        return this.width * this.height;
    }
}
// extends를 쓰면 Shape에서 정의한 것들을 자동적으로 Rectangle에 포함됨
class Rectangle extends Shape {}
// 필요한 함수만 재정의 할 수 있음 : 오버라이딩
class Triangle extends Shape {
     draw() {
         super.draw(); // 원래 draw()함수도 호출됨
        console.log('🔺');
    }
    getArea() {
        return this.width * this.height / 2;
    }
    // Object의 메소드 오버라이딩
    toString() {
        return `Triangle: color: ${this.color}`;
    }
}
const rectangle = new Rectangle(20,20,'blue');
rectangle.draw(); // drawing blue color!
console.log(rectangle.getArea()); // 400
const triangle = new Triangle(20,20,'red');
triangle.draw(); //  drawing red color!;🔺
console.log(triangle.getArea()); // 200

//6. class checking instanceOf
// 왼쪽의 instance가 오른쪽의 class의 object인지아닌지 boolean
console.log(rectangle instanceof Rectangle); // true
console.log(triangle instanceof Rectangle); // false
console.log(triangle instanceof Triangle); // true
console.log(triangle instanceof Shape); // true
// js의 모든 인스턴스는 Object를 상속함
console.log(triangle instanceof Object); // true
// Object의 공통적인 method를 쓸 수있음
console.log(triangle.toString()); // [object Object] -> Triangle: color: red(오버라이딩되면 이렇게 바뀜)
```



### Object

``` js
// 선언 object = { key : value };
const obj1 = {}; //object literal syntax
const obj2 = new Object(); // object contructor syntax
// Objects
function print(person) {
    console.log(person.name);
    consle.log(person.age);
}
const iris = { name:'iris', age:20};
print(iris); // iris; 20

// js는 아래처럼 따로 추가할 수도 있음 -> 하지만 이렇게 하면 유지보수가 어려우니 되도록이면 쓰지말자
iris.hasJob = true;
console.log(iris.hasJob); // true
delete iris.hasJob;
console.log(iris.hasJob); // undefinded

// 2. Computed properties : ['key']
// key는 string 타입이어야 됨
// '.' -> coding할때 그 key에 대한 value를 가져오고 싶을때 사용
// '['key']' -> 어떤 key가 필요한지 모를때, runtime에서 결정될때 사용됨
console.log(iris.name); // iris
console.log(iris['name']); //iris
iris['hasJob'] = true;
console.log(iris.hasJob); // true
// 예
// key값을 모를때
function printValue(obj, key) {
    // object에 key라는 property가 들어있니?
    console.log(obj.key);
}
printValue(iris, 'name'); // undefinded
// 동적으로 key에 대한 value를 가져오고 싶을 떄 computed properties사용
function printValue(obj, key) {
    console.log(obj[key]);
}
printValue(iris, 'name'); // iris
printValue(iris, 'age'); // 20

// 3. property value shorthand
const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };

// 4. Constructor function
const person4 = new Person('iris',20);
console.log(person4); // Person {name:'iris',age:20}
// 순수하게 object를 생성하는 함수는 이름이 대문자(class같은 역할을 함)
function Person(name,age) {
    // 생략된 코드
    // this = {};
    this.name = name;
    this.age = age;
    // return this;
}

// 5. in operator 해당 obj에 key가 있는지 없는지 확인
console.log('name' in iris); // true
console.log('age' in iris); // true
console.log('random' in iris); // false
console.log(iris.random); // undefinded

// 6. for..in vs for..of
// for (key in obj)
// 이전 콘솔 지움 console.clear();
// iris의 모든 key 출력
for (key in iris) {
    console.log(key); // name; age; hasJob
}
// for (Value of iterable)
const array = [1,2,4,5];
// 보통 for문
for (let i = 0; i < array.length; i++) {
    console.log(array[i]); // 1;2;4;5
}
// for of 이용 -> value가 순차적으로 나옴
for (value of array) {
    console.log(value); // 1;2;4;5
}

// 7. cloning
const user = {name:'iris', age:'20'};
const user2 = user; // user2에도 user와 똑같은 reference가 할당됨
user2.name = 'coder';
console.log(user);  // {name:'coder',age:'20'} -> user2를 바꿨지만 user도 바뀜!(reference가 같기 때문)
// 원본에 영향을 주지않는 복사 방법
// 1)old way 
const user3 = {};
for (key in user) { // key : name, age
    user3[key] = user[key];
}
console.log(user3); //{name:'coder',age:'20'}

// 2) Object.assign(dest,[obj1,obj2,obj3...])
const user4 = Object.assign({}, user);
console.log(user4) //{name:'coder',age:'20'}

// another example
const fruit1 = {color : 'red'};
const fruit2 = {color:'blue', size:'big'};
// 뒤에적을수록 앞의 key가 동일한게 있으면 앞의 값이 오버라이딩됨
const mixed = Object.assign({},fruit1,fruit2);
console.log(mixed.color); // blue
console.log(mixed.size); // big
```



## Array

> 한배열에는 동일한 type만 들어가야된다!(JS에서는 동일한 type이 아니어도 들어가지만 그렇게 코딩하는건 좋지않다!)

```js
'use strict';

// Array
// 1. 선언
const arr1 = new Array();
const arr2 = [1,2];
// 2. index
const fruits = ['사과','바나나'];
console.log(fruits); // ['사과','바나나'] -> 0:'사과'; 1:'바나나'; length:2
console.log(fruits.length);  //2
// console.log(fruits[index])로 접근가능
// 배열의 첫번째 index = 0, 마지막index = fruits.length-1
console.log(fruits[0]); // 사과
console.log(fruits[1]); // 바나나
console.log(fruits[2]); // undefinded

// 3. Looping
// 1) for loop
for (let i=0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
// 2) for of
for (let fruit of fruits) {
    console.log(fruit);
}
// 3) forEach(ctrl+click하면 공식문서나옴)
fruits.forEach((fruit) => console.log(fruit));

// 4. 삽입, 삭제, 복사
// push : add item to the end
fruits.push('딸기','복숭아');
console.log(fruits); // ['사과','바나나','딸기','복숭아']
// pop:remove an item from the end -> 지워지는 값이 return됨
fruits.pop(); 
// const poped = fruits.pop(); //'복숭아'
console.log(fruits) //  ['사과','바나나','딸기']
// unshift : add an itme to the beginning
fruits.unshift('복숭아');
console.log(fruits) //  ['복숭아',사과','바나나','딸기']
// shift : remove an itme to the beginning
fruits.shift();
console.log(fruits) //  [사과','바나나','딸기']

// ⭐⭐shift와 unshift는 pop,push보다 느리다!
// why?? 뒤에것을 빼거나 추가하는건 다른 data는 변화없지만 shift와 unshift는 앞에 넣었다가 빼기 때문에 다른 data의 index변화가 있음

// splice : remove an item by index position
fruits.push('복숭아','레몬');
console.log(fruits); // ['복숭아','레몬',사과','바나나','딸기']
// splice(어느 index에서 시작, 몇개,'추가할데이터1','추가할데이터2'..) 만약 몇개를 지정하지 않는다면 해당 index부터 전부 삭제, 0을 적으면 삭제되지 않음+ 해당 index에 추가할데이터 1, 추가할데이터 2가 추가됨
fruits.splice(1,1,'수박','포도');
console.log(fruits); // ['복숭아','수박','포도',사과','바나나','딸기']

// concat : combine two arrays
const fruits2 = ['배','키위'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits); // ['복숭아','수박','포도',사과','바나나','딸기','배','키위']

// 5. searching
// indexOf : find the index (제일첫번째로 해당하는 index값 반환)
console.log(fruits);// ['복숭아','수박','포도',사과','바나나','딸기']
console.log(fruits.indexOf('사과')); // 3
console.log(fruits.indexOf('수박')); // 1
console.log(fruits.indexOf('멜론')); // -1 : 없는값은 -1 출력
// includes : 배열에 있는지 없는지 true/false
console.log(fruits.includes('수박')); // true
// lastIndexOf : find the index (제일 마지막에 해당하는 index값 반환)
fruits.push('사과');
console.log(fruits); //['복숭아','수박','포도',사과','바나나','딸기','사과']
console.log(fruits.indexOf('사과')); // 3
console.log(fruits.lastIndexOf('사과')); // 6
```



