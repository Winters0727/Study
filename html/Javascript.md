# Javascript 정리(w3cschools.com)

**자바스크립트는 HTML 컨텐츠를 바꿀 수 있다.**

자바스크립트의 주요 HTML 메서드로 `getElementById()` 가 있다.

`getElementById()`는 HTML의 요소를 `id = 'demo'`로 찾아 요소의 내용을 변경할 수 있다.

``````javascript
document.getElementById("demo").innerHTML = "Hello JavaScript"
``````

실제 HTML에 적용해보면 다음과 같다.

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h2>
            자바스크립트 예시입니다.
        </h2>
        <p id="demo">자바스크립트는 HTML 컨텐츠를 바꿀 수 있습니다.</p>
        <button type="button" onclick='document.getElementById("demo").innerHTML = "안녕, 자바스크립트!"'>이걸 눌러봐!</button>
    </body>
</html>
``````

자바스크립트는 홑따옴표`''`, 쌍따옴표`""` 모두 사용이 가능하다.



**자바스크립트는 HTML 인자의 값도 변경이 가능하다.**

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>

        <h2>자바스크립트 예시입니다.</h2>
        <p>자바스크립트로 HTML 인자의 값도 변경이 가능합니다.</p>
        <p>자바스크립트로 이미지를 변경해봅시다.</p>

        <button onclick="document.getElementById('이미지 id').src='이미지 주소'">첫번쨰 이미지로 변경</button>

        <img id="이미지 id" src="이미지 주소" style="width:100px">

        <button onclick="document.getElementById('이미지 id').src='이미지 주소'">두번째 이미지로 변경</button>

    </body>
</html>
``````



**자바스크립트는 CSS 컨텐츠를 바꿀 수 있다.**

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h2>
            자바스크립트 예시입니다.
        </h2>
        <p id="demo">
            자바스크립트로 CSS 컨텐츠를 바꿀 수 있습니다.
        </p>
        <button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">
            이걸 눌러봐!
        </button>
    </body>
</html>
``````



**자바스크립트는 HTML 컨텐츠를 숨기고, 보여줄 수 있습니다.**

``````html
<!DOCTYPE>
<html>
    <head>
        
    </head>
    <body>
        <h2>
            자바스크립트 예시입니다.
        </h2>
        <p id="demo">
            자바스크립트로 HTML 컨텐츠를 숨기고, 보여줄 수 있습니다.
        </p>
        <button type="button" onclick="document.getElementById('demo').style.display='block'">
            이걸 누르면 보인다!
        </button>
        <button type="button" onclick="document.getElementById('demo').style.display='none'">
            이걸 누르면 없어진다!
        </button>
    </body>
</html>
``````



### 자바스크립트 사용

**\<script> 태그**

HTML에서 자바스크립트 코드는 \<script>\</script> 태그 사이에 작성한다.

``````html
<script>
document.getElementById("demo").innerHTML = "내 첫 자바스크립트!"
</script>
``````



**자바스크립트의 함수와 이벤트**

자바스크립트에서 함수는 호출되는 코드블럭을 의미하고, 함수는 사용자에 의한 이벤트 발생에 의해 호출된다.



**자바스크립트에서의 \<head>와 \<body> 태그**

자바스크립트 코드는 \<head>, \<body> 태그 둘 다 적용이 가능하다.

``````html
<!DOCTYPE>
<html>
    <head>
        <script>function myFunction() {
            document.getElementById("demo").innerHTML="짜잔! 내용이 바뀌었습니다!";
            }</script>
    </head>
    <body>
        <h2>
            head 태그에 스크립트 구문이 포함되어있습니다.
        </h2>
        <p id="demo">
            내용이 바뀔 문단입니다.
        </p>
        <button type="button" onclick="myFunction()">
            눌러볼래?
        </button>
    </body>
</html>
``````

``````html
<!DOCTYPE>
<html>
    <head>

    </head>
    <body>
        <h2>
            body 태그에 스크립트 구문이 포함되어있습니다.
        </h2>
        <p id="demo">
            내용이 바뀔 문단입니다.
        </p>
        <button type="button" onclick="myFunction()">
            눌러볼래?
        </button>
        <script>function myFunction() {
            document.getElementById("demo").innerHTML="짜잔! 내용이 바뀌었습니다!";
            }</script>
    </body>
</html>
``````



**외부에서 자바스크립트 파일 불러오기**

``````javascript
function myFunction() {
    document.getElementById("demo").innerHTML="짜잔! 내용이 바뀌었습니다.";
}
``````

외부에 저장되어있는 자바스크립트 파일을 `myScript.js`라 하자. 자바스크립트 파일의 확장자는 `.js`이다.

자바스크립트 파일은 `<script>` 태그의 `src`인자를 통해 HTML로 불러올 수 있다.

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <script src="myScript.js"></script> <!--단, 외부에서 자바스크립트 파일을 가져온 스크립트 태그에는 내용을 채워서는 안된다.-->
    </body>
</html>
``````

외부에서 자바스크립트 파일을 불러오면 다음과 같은 장점을 가진다.

- HTML 코드와 분리 가능하다.
- HTML과 자바스크립트 파일을 각각 보수, 관리하기 편하게 만들어준다.
- 캐싱된 자바스크립트 파일은 페이지를 더 빠르게 불러올 수 있다.

다음과 같이 HTML파일 내에 여러개의 자바스크립트 파일을 불러올 수 있다.

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <script src="myScript1.js"></script>
        <script src="myScript2.js"></script>
    </body>
</html>
``````



### 자바스크립트를 통한 HTML 컨텐츠 변경

자바스크립트는 다양한 방법을 통해 데이터를 보여줄 수 있다.

- HTML 요소를 변경하려면 `innerHTML`
- HTML 결과물을 사용하려면 `document.write()`
- 경고 박스를 띄우려면 `window.alert()`
- 브라우저 콘솔을 불러오려면 `console.log()`



**innerHTML**

HTML 요소에 접근하기위해 자바스크립트에서는 `document.getElementById(id)` 메서드를 제공한다.

`id`는 HTML 요소의 인자이며, `innerHTML`을 통해 HTML 컨텐츠를 정의할 수 있다.

``````html
<p id="demo"></p> <!--자바스크립트 코드로 인해 내용이 변경될 문단-->
<script>document.getElementById("demo").innerHTML="내용을 변경합니다.";</script>
``````



**document.write()**

HTML 요소에 상관없이 HTML의 컨텐츠를 바꾸는 방법으로 `document.write()`가 있다.

``````html
<script>document.write("내용을 추가합니다.");</script>
``````

단, `document.write()`는 HTML 문서의 로딩이 끝난 뒤에 일어나므로 문서에 먼저 존재하는 HTML 내용은 지워진다. 따라서, `document.write()`는 테스트 용도로만 사용할 것을 권고한다.



**window.alert()**

현재 표시중인 데이터에서 경고창을 보여준다.

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <script>window.alert("경고 : 자바스크립트에서 경고를 보냅니다.");</script>
    </body>
</html>
``````



**console.log()**

디버깅 목적으로 사용되는 메서드이다.

``````html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        console.log(변수명);
    </body>
</html>
``````



### 자바스크립트 문장

**자바스크립트 프로그램**

자바스크립트는 웹 브라우저를 동작시키는 프로그래밍 언어다.

자바스크립트 문장은 다음과 같이 구성된다.

`[변수(values), 연산자(operators), 표현식(expressions), 키워드(keywords), 주석(comments)]`

자바스크립트는 한 문장씩 읽혀지며, 작성된 순서에 따라 작동한다.



**세미콜론 ;**

자바스크립트 문장에서 세미콜론은 문장을 구분하는 역할을 한다. (즉, 문장의 끝임을 의미한다.)

``````javascript
var a, b, c; // 3개의 변수를 선언한다.
a = 5; // a에 5를 할당한다.
b = 6; // b에 6을 할당한다.
c = a + b; // c에 a와 b의 합을 할당한다.
``````

세미콜론을 활용하면 다음과 같이 한줄로 표현이 가능하다.

``````javascript
var a, b, c;
a = 5; b = 6; c = a + b;
``````



**빈칸(white space)**

자바스크립트는 빈칸을 무시한다. 하지만 가독성을 위해서 빈칸을 넣어주는 것이 좋다.

특히 연산자를 사용할 때 빈칸을 넣어주면 가독성에 좋다.

``````javascript
var x = y + z;
``````



**문장의 길이와 줄바꿈**

좋은 가독성을 위해서 프로그래머는 보통 80자를 넘기지 않는다.

자바스크립트 문장이 한줄에 다 들어가지 않을 경우, 연산자 뒤에 줄바꿈을 하는 것이 가독성을 위해 좋다.

``````javascript
document.getElementById("demo").innerHTML = 
"안녕, 돌리!"
``````



**코드 블럭 {…}**

자바스크립트의 문장들은 코드 블럭으로 묶일 수 있다. 코드 블럭의 목적은 문장들이 함께 작동시키기 위함이다.

``````javscript
function myFunction() {
    document.getElementById("demo1").innerHTML = "안녕, 돌리!";
    document.getElementById("demo2").innerHTML = "잘 지내니?";
}
``````



### 자바스크립트 키워드

자바스크립트에는 특정 작동을 수행하기 위한 키워드가 존재한다.

자바스크립트의 모든 키워드를 보고싶다면 <a href="https://www.w3schools.com/js/js_reserved.asp">여기</a>를 참조하자.

다음은 다음 내용에서 배우게 될 키워드에 대한 간략한 설명이다.

| **키워드**  |                           **설명**                           |
| :---------: | :----------------------------------------------------------: |
|    break    |              스위치나 반복(loop)을 종료시킨다.               |
|  continue   | 현재 실행되고 있는 반복문을 건너뛰고, 반복문의 시작지점으로 돌아간다. |
|  debugger   | 자바스크립트의 작동을 중지시키고 (가능하다면) 디버깅 함수를 호출한다. |
| do … while  | do 이후의 코드블럭을 1회 실행하고, while 이후의 조건을 만족하면 반복실행한다. |
|     for     |         조건을 만족하는 한 코드블럭을 반복실행한다.          |
|  function   |                       함수를 선언한다.                       |
|  if … else  |    조건을 만족하면(논리적 참, true) 코드블럭을 실행한다.     |
|   return    |                      함수를 빠져나온다.                      |
|   switch    |        여러 경우(케이스)에 따라 다른 코드를 실행한다.        |
| try … catch |       코드 블럭에 있는 문장에 에러 핸들링에 적용한다.        |
|     var     |                       변수를 선언한다.                       |

