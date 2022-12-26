# [beebox]HTML Injection - Reflected (URL)

## Level. low

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(URL)%20-%201.png)

패킷을 잡아 html 구문을 삽입합니다.

```html
<h1>Success</h1>
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(URL)%20-%202.png)

성공!

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(URL)%20-%203.png)

여기서 잠깐 왜 직접 URL에 넣지 않고 패킷을 잡아 넣는가?

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(URL)%20-%204.png)

URL에 직접 입력하면 브라우저에서 특수문자를 URL 인코딩하여 요청을 보내기 때문입니다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(URL)%20-%205.png)

<br>

## Level. high

htmlspecialchars 함수를 이용하기 때문에 <, >, &, ', " 가 필터링 됩니다.