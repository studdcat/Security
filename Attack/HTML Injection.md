# 📍 HTML Injection

취약한 매개변수에 악의적인 HTML 코드를 삽입하여 사용자가 의도하지 않은 페이지를 보여주거나 악성 사이트로 연결 시킬 수 있습니다.

GET, POST, Stored 3가지의 공격 방법이 있습니다.

<br>

### GET(Reflected)

GET 방식으로 값을 헤더로 통해 전달할 때 발생합니다.

URL 뒤에 코드를 삽입하기 떄문에 데이터양은 제한적입니다.

<br>

### POST(Reflected)

POST 방식으로 값을 바디로 통해 전달할 때 발생합니다.

바디로 값을 전달하기 때문에 많은 데이터양을 보낼 수 있습니다.

<br>

### Stored

악의적인 HTML 코드를 DB에 저장하여 사용자 PC에서 HTML 태그가 실행되게합니다.

다수의 피해자가 발생할 수 있습니다.

<br>

## ⚔ Offensive techniques

``` html
<h1>

<h1>Success</h1>

<img src="/images/~~~">

<img src=">

<form action="<textarea>

<a href="https://www.naver.com">Click</a>

<base href="https://www.naver.com">

<meta http-equiv="refresh" content="0;url=https://www.naver.com">
```

<br>

## 🔒 Denfensive techniques

htmlspecialchars는 특수문자(&, ", ', <, >)를 UTF-8로 반환한다.

htmlspecialchars는 함수를 이용하여 특수문자를 UTF-8로 인코딩한다.

<br>

## Reference

https://www.invicti.com/learn/html-injection/