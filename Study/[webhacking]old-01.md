# [webhacking]old-01

![](../img/Study%20Img/%5Bwebhacking%5Dold-01%20-%201.png)

view-source 클릭

php 코드가 나온다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-01%20-%202.png)

이 중에 밑 코드를 살펴보자.

```php
<?php
  if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;
  if($_COOKIE['user_lv']>=4) $_COOKIE['user_lv']=1;
  if($_COOKIE['user_lv']>3) solve(1);
  echo "<br>level : {$_COOKIE['user_lv']}";
?>
```

_COOKIE['user_lv'] 의 값이 숫자가 아니면 =1 이 된다.

```php
  if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;
```

여기서 user_lv 는 쿠키 값을 말한다.

즉, 쿠키 값이 숫자가 아니면 _COOKIE['user_lv'] 는 1이 된다.

![](../img/Study%20Img/%5Bwebhacking%5Dold-01%20-%203.png)

level : _COOKIE['user_lv'] 를 화면에 출력한다. 실제로 쿠키 값에 따라 출력된다.

```php
  echo "<br>level : {$_COOKIE['user_lv']}";
```

user_lv 가 4보다 크거나 같으면 _COOKIE['user_lv'] = 1이 된다.

user_lv 가 3보다 크면 solve(1) 함수를 실행한다. 아마 성공을 뜻하는 함수일 것이다.

```php
  if($_COOKIE['user_lv']>=4) $_COOKIE['user_lv']=1;
  if($_COOKIE['user_lv']>3) solve(1);
```

그렇기에 우리는 쿠키 값을 3보다 크지만 4보다는 작게 해야한다.

3.5 입력

![](../img/Study%20Img/%5Bwebhacking%5Dold-01%20-%204.png)

![](../img/Study%20Img/%5Bwebhacking%5Dold-01%20-%205.png)

나는 이미 풀어서 이런 메세지가 나오지만 처음 풀면 성공 메세지가 나올 것이다.

<br><br>

---
쿠키 값 변조 문제인듯 

분류하자면 쿠키 및 세션 인증 취약점인듯