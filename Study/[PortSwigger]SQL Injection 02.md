# [PortSwigger]SQL Injection 02

https://portswigger.net/web-security/all-labs

## LAB
로그인 우회를 허용하는 SQL Injection 취약점

## Qusetion
이 랩에는 로그인 기능에 SQL 인젝션 취약점이 포함되어 있습니다.

## Solution

로그인에 SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2002%20-%201.png)

<br>

ID 부분을 참이 되게 하고 뒷 부분은 주석 처리해 비밀번호는 검증하지 않게함 
```
' or 1=1 --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2002%20-%202.png)

<br>

성공적으로 로그인이 된 모습

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2002%20-%203.png)