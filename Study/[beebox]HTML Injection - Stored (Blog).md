# [beebox]HTML Injection - Stored (Blog)

## Level. low

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%201.png)

HTML injection - Reflected (POST)의 코드를 이용해 보자.

```html
<form action="/bWAPP/htmli_post.php" method="POST">

        <p><label for="firstname">First name:</label><br />
        <input type="text" id="firstname" name="firstname"></p>

        <p><label for="lastname">Last name:</label><br />
        <input type="text" id="lastname" name="lastname"></p>

        <button type="submit" name="form" value="submit">Go</button>  

    </form>
```

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%202.png)

입력칸에 코드를 입력한다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%203.png)

htmli_post.php 에서 볼수 있던 입력 칸이 출력된다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%204.png)

값을 넣는다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%205.png)

htmli_post.php 에 값이 들어가는 것을 확인 할수 있다. 성공!

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%206.png)

<br>

## Level. medium, high

htmlspecialchars 함수로 필터링 하기 때문에 값이 그대로 나오는 것을 확인 할수있다.

HTML Injection은 htmlspecialchars 함수로 막으면 된다.

![](../img/Study%20Img/%5Bbeebox%5DHTML%20Injection%20(Blog)%20-%207.png)