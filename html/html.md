HTML 정리(w3schools.com)

### html 기본형

``````html
<!DOCTYPE html> <!-- html은 대소문자 구분을 하지 않는다. -->
<html> <!-- whole document -->
    <head> <!-- header -->
    
    </head>
    <body> <!-- document body -->
    
    </body>
</html> <!-- Make sure do not forget the end tag!!! -->
``````



### 기본 코드

> ``````html
> <tagname>Content goes here...</tagname>
> ``````
>
> ``````html
> <h#></h#> <!--(#1~6) : 글씨 크기 + Bold, 숫자가 클수록 작아짐.-->
> 
> <a href="link">link</a> <!--: 글씨를 누르면 해당 link로 이동-->
> 
> <img src="img_source" alt = "img_text" width="" height=""> <!--: 이미지 삽입-->
> 
> <button>button</button> <!--: 버튼 삽입-->
> 
> <ul> <!--: 순서 없는 리스트 -->
>     <li></li> <!--: 리스트값 입력 -->
> </ul>
> <ol> <!--: 순서 있는 리스트 -->
>     <li></li>
> </ol>
> <br> <!--: 줄바꿈 (Empty elements) -->
> ``````



### html attributes

> ``````html
> <img src="" width="" height="" alt=""> <!--:이미지 주소, 넓이, 높이, 대체 텍스트 -->
> <p style="color:red">This is a paragraph with an red color.</p> <!--: 문항의 색, 폰트, 크기 변경 -->
> <html lang="en-US"></html> <!--: 언어 설정 -->
> <p title=""></p> <!--: 마우스가 해당 문항 위에 있을 때 출력 -->
> ``````
>
> | Attribute | Description                                    |
> | --------- | ---------------------------------------------- |
> | alt       | 이미지가 나오지 않을 경우에 출력될 대체 텍스트 |
> | disabled  | 사용되지 않아야할 입력값 설정                  |
> | href      | URL 주소로의 링크                              |
> | id        | 요소의 id를 설정                               |
> | src       | 이미지 URL 주소                                |
> | style     | 요소의 CSS 스타일 정의                         |
> | title     | 요소의 추가 정보                               |



### html headings

> - heading은 '<h#>'으로 정의되고, #의 범위는 1~6이다.
>
> - heading은 요소의 중요도를 나타내며, 문자의 크기를 키우거나 Bold체를 사용해서는 안된다.
> - 그래도 heading의 크기를 변경하려면 style 인자를 활용하면 된다.
>
> ``````html
> <h1 style="font-size=60px">Change heading 1</h1>
> ``````
>
> ``````html
> <html>
>     <head> <!-- : html metadata의 정보를 저장하는 태그로, metadata는 숨겨진다.-->
>         <meta charset="UTF-8">
>     </head>
>     <body>
>         <hr> <!-- : 수평선을 그어 내용을 구분할 때 사용한다. -->
>     </body>
> </html>
> ``````
>
> | Tag            | Description                                               |
> | -------------- | --------------------------------------------------------- |
> | \<html>        | html 문서임을 의미                                        |
> | \<body>        | 문서의 내용을 담는 곳                                     |
> | \<head>        | head 요소를 담는 곳(title, script, styles, metadata etc.) |
> | \<h1> to \<h6> | html headings                                             |
> | \<hr>          | 수평선을 그어 내용을 구분                                 |



### html paragraphs

> ``````html
> <html>
>     <head>
>         
>     </head>
>     <body>
>         <p> <!-- : 한 내용을 담는 문항-->
>             Hello, html! <br> <!-- : 문장을 끝내고, 다음 줄로 이동-->
>         </p>
>         <pre> <!-- : 미리 정의된 형태로 출력-->
>             이 문장은 있는 그대로 보여집니다.
>         </pre>
>     </body>
> </html>
> ``````
>
> | Tag    | Description                                   |
> | ------ | --------------------------------------------- |
> | \<p>   | 문항을 정의                                   |
> | \<br>  | 한 줄 바꾸기                                  |
> | \<pre> | 문장을 미리 정의된 형태(pre-formatted)로 출력 |



### html style Attributes

> style 인자는 다음과 같은 문법을 따른다.
>
> ```````html
> <tagname style="property:value;"></tagname>
> ```````
>
> *property*는 CSS의 property고, *value*는 CSS의 value이다.  
>
> ``````html
> <html>
>     <head>
>         
>     </head>
>     <body style="background-color:powderblue;"> <!-- : 배경색 지정-->
>         <h1 style="color:blue;">This is a heading.</h1> <!-- : 글자색 지정-->
>         <p style="color:red;">This is a paragraph.</p>
>         <br>
>         <h1 style="font-family:verdana;">This is a heading.</h1> <!-- : 글자 font 지정-->
>         <p style="font-family:corier;">This is a paragraph.</p>
>         <br>
>         <h1 style="font-size:300%;">This is a heading.</h1> <!-- : 글자 크기 지정-->
>         <p style="font-size:160%;">This is a paragraph.</p>
>         <br>
>         <h1 style="text-align:center;">This is a heading.</h1> <!-- : 글자 정렬-->
>         <p style="text-align:center;">This is a paragraph.</p>
>     </body>
> </html>
> ``````
>
> | Style            | Description    |
> | ---------------- | -------------- |
> | background-color | 배경색 지정    |
> | color            | 글자색 지정    |
> | font-family      | 글자 font 지정 |
> | font-size        | 글자 크기 지정 |
> | text-align       | 글자 정렬      |



### text formatting

> ``````html
> <html>
>     <head>
>     </head>
>     <body>
>         <b></b> <!-- : 글자에 bold 효과-->
>         <strong></strong> <!-- : 글자에 bold 효과 및 의미적으로 'strong' 중요도-->
>         <i></i> <!-- : 글자에 이탤릭체 효과-->
>         <em></em> <!-- : 글자에 이탤릭체 효과 및 의미적으로 'emphasized' 중요도-->
>         <big></big> <!-- : 같은 태그 내에서 글자를 더 크게 만듦-->
>         <small></small> <!-- : 같은 태그 내에서 글자를 더 작게 만듦-->
>         <mark></mark> <!-- : 글자를 색으로 줄을 그어 강조 효과-->
>         <del></del> <!-- : 글자에 줄을 그어 삭제된 효과-->
>         <ins></ins> <!-- : 글자 아래에 밑줄 긋기 효과-->
>         <sub></sub> <!-- : 글자 아랫첨자-->
>         <sup></sup> <!-- : 글자 윗첨자-->
>     </body>
> </html>
> ``````
>
> | Tag       | Description                   |
> | --------- | ----------------------------- |
> | \<b>      | bold 효과                     |
> | \<strong> | bold 효과 + 의미 강조         |
> | \<em>     | 이탤릭체 효과 + 의미 강조     |
> | \<i>      | 이탤릭체 효과                 |
> | \<big>    | 글자 크기를 크게              |
> | \<small>  | 글자 크기를 작게              |
> | \<sub>    | 아랫첨자                      |
> | \<sup>    | 윗첨자                        |
> | \<ins>    | 밑줄 긋기                     |
> | \<del>    | 취소선                        |
> | \<mark>   | 색줄을 그어 강조(highlighted) |



### html Quotation and Citation

> ``````html
> <html>
>     <head>
>     
>     </head>
>     <body>
>         <q>인용구입니다.</q> <!-- : 문장 인용구, 쌍따옴표-->
>         <blockquote cite="url"> <!-- : 인용구로 cite인자로 출처표기, 들여쓰기-->
>             들여쓰기 문장입니다.
>         </blockquote>
>         <p>
>             <abbr title="Samsung Software Academy For Youth">SSAFY</abbr>가 무엇의 약자인줄 아시나요? <!-- : 축약어, title 인자로 축약어의 의미 추가 가능-->
>         </p>
>         <address> <!-- : 주소를 인용할 때 사용, 이탤릭체로 표기-->
>             주소를 작성합니다.<br>
>             서울특별시 강남구 역삼동 테헤란로 212<br>
>             1588-3357
>         </address>
>         <p>
>             <cite> <!-- : 한줄 인용, 이탤릭체로 표기-->
>                 인용 문장입니다.
>             </cite>
>         </p>
>         <p>
>             이 문장은 왼쪽에서 오른쪽으로 작성됩니다.<br>
>             <bdo dir="rtl">이 문장은 오른쪽에서 왼쪽으로 작성됩니다.</bdo> <!-- : bi-directional override로 문장 요소의 텍스트 방향성을 정의할 때 사용-->
>         </p>
>     </body>
> </html>
> ``````
>
> | Tag           | Description                    |
> | ------------- | ------------------------------ |
> | \<abbr>       | 축악어 설명                    |
> | \<address>    | 작성자나 주인의 연락 정보      |
> | \<bdo>        | 텍스트 방향 설정               |
> | \<blockquote> | 다른 출처로부터 가져온 글 인용 |
> | \<cite>       | 한줄 인용                      |
> | \<q>          | 인용기호(쌍따옴표)             |