# [webhacking]old-03

https://webhacking.kr/

https://poci.tistory.com/103

<br>

화면에 숫자와 정사각형이 있다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%201.png)

빈 사각형 5 x 5 의 크기는 클릭이 가능했고 누를 때 검정색 하얀색이 반복으로 보여진다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%204.png)

어렸을 적했던 네모네모로직을 기억을 되살려 문제 풀이는 성공했다.

파라미터 값은 저렇게 넘어갔다.

파라미터 변조에도 반응이 없거나 index.php 페이지로 이동되었다. (지워보기도 하고 SQL 구문도 넣어봤음)

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%202.png)

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%203.png)

클리어가 되었다고 한다. 나의 로그? 입력 일단 입력했다.

입력 > 8DD

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%205.png)

성공메시지는 보이지 않고 화면처럼만 출력됐다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%206.png)

입력칸에 SQL Injection, XSS, Command 등 해봤지만 반응 없었다. 값 그대로 넘어갔다.

```
' or 1=1--
' and 1=1--
' and 1=0--

<script>alert(document.cookie)</script>

| ../../../../../etc/passwd
```

버프로 패킷을 잡고 파라미터 answer에 SQL Injection 시도


![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%207.png)

```
answer=' or 1=1--공백(%20)
```

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%208.png)

성공 !!!

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%209.png)

![](../img/Study%20Img/%5Bwebhacking%5Dold-03%20-%2010.png)