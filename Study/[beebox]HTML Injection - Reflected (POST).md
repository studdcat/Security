# [beebox]HTML Injection - Reflected (POST)

## Level. low

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%201.png)

GET 방식이 아닌 POST 방식으로 파라미터가 아닌 body로 값이 넘어가기 때문에 URL에는 값이 보이지 않는다.

값은 제대로 들어간다.

```
First name = 123
Last name = 456
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%202.png)

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%203.png)

중간 패킷을 잡는 도구인 burp suite의 proxy 기능을 이용해서 패킷을 확인해 보겠다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%204.png)

body 부분으로 값이 넘어가는거 확인. body 부분의 값을 조작해서 공격을 시도해 보겠다.

```
firstname=<h1>Success</h1>&lastname=<img%20src='http://192.168.200.177/bWAPP/images/bee_1.png'>
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%205.png)

성공 !!

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%209.png)


## Level. medium

난이도 low 의 방법은 문자열 그대로 나온다. "< >" 필터링 되고 있기 때문이다.

우회하기 위해 URL 인코딩 %3c %3e 로 바꿔 공격해 본다.

```
firstname=%3ch1%3eSuccess%3c/h1%3e&lastname=%3cimg%20src='http://192.168.200.177/bWAPP/images/bee_1.png'%3e
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%2010.png)

문자열 그대로 나오는 모습이다.

%3c %3e 값을 그대로 입력해봤더니 %253c %253e 가 나왔다.

더블 인코딩이 된 모습이다.

더블 인코딩이란 인코딩된 단계에서 한번더 인코딩을 한것이다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%2011.png)

더블 인코딩을 해서 값을 넣어본다.

```
firstname=%253ch1%253eSuccess%253c/h1%253e&lastname=%253cimg%20src='http://192.168.200.177/bWAPP/images/bee_1.png'%253e
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%2012.png)

성공 !!!

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(POST)%20-%209.png)

## Level. high

난이도 high는 GET 방식과 마찬가지로 htmlspecialchars 함수를 이용하기 때문에 <, >, &, ', " 가 필터링 된다.

따라서 HTML Injection의 대응방안으로는 htmlspecialchars 함수를 적용시키는 것이다.