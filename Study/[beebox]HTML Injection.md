# [beebox]HTML Injection

HTML Injection은 HTML 필터링 없이 값을 그대로 가져다 쓰기 때문에 발생하며, 원치않는 내용을 보게하거나 사이트로 이동킨다.

## Level. Low

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%201.png)

입력칸 두 곳에 값을 입력해야 출력이 되며 GET 방식을 이용하고 있다.

URL에 파라미터 값이 다 노출된다.

```
<h1>Success</h1>

<img src="http://192.169.200.177/bWAPP/images/bee_1.png">
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%202.png)

ip 주소는 본인 ip를 넣으면 된다. 나는 호스트 PC(로컬)에서 실습 중이다.

이처럼 넣은 값 그대로 나오는 모습이다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%203.png)