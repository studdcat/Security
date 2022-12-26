# [beebox]HTML Injection - Reflected (GET)

## 🍟 HTML?

취약한 매개변수에 악의적인 HTML 코드를 삽입하는 공격이다.

HTML Injection은 HTML 필터링 없이 값을 그대로 가져다 쓰기 때문에 발생하며, 원치않는 내용을 보게하거나 사이트로 이동킨다.

<br>

## Level. low

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%201.png)

입력칸 두 곳에 값을 입력해야 출력이 되며 GET 방식을 이용하고 있다.

URL에 파라미터 값이 다 노출된다.

```
<h1>Success</h1>

<img src="http://192.168.200.177/bWAPP/images/bee_1.png">
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%202.png)

ip 주소는 본인 ip를 넣으면 된다. 나는 호스트 PC(로컬)에서 실습 중이다.

이처럼 넣은 값 그대로 나오는 모습이다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%203.png)

<br>

## Level. medium

```
<h1>Success</h1>

<img src="http://192.168.200.177/bWAPP/images/bee_1.png">
```

필터링이 존재해서 문자열 그대로 출력된다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%204.png)

< 와 > 꺽새들을 URL 인코딩을 하여 다시 입력해본다.

URL 인코딩 값은 < = %3c, > = %3e

인코딩은 구글에 치면은 자동으로 변환해주는 사이트들이 많이 나온다 직접해보자.

```
%3ch1%3eSuccess%3c/h1%3e

%3cimg src="http://192.168.200.177/bWAPP/images/bee_1.png"%3e
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%205.png)

<br>

## Level. high

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20-%206.png)


```php
function xss_check_3($data, $encoding = "UTF-8")
{
    return htmlspecialchars($data, ENT_QUOTES, $encoding);
}
```

low, medium에서 입력 했던 값으로 해도 문자열 그대로 나온다. 태그를 입력해도 태그로 해석되지 않는 이유는 우회단계를 거쳤기 때문이다.

HTML을 근본적으로 막을 수 있는 방법은 php 에서 기본적으로 제공하는 함수인 htmlspecialchars 함수를 이용하면 <,>,',",& 특수문자를 UTF-8로 변환한다.

따라서 HTML Injection을 막으려면 htmlspecialchars 함수를 사용하여 특수문자들을 인식하지 않게 인코딩하는 것이다.