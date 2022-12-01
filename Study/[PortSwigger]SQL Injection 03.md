# [PortSwigger]SQL Injection 03

https://portswigger.net/web-security/all-labs

## LAB
쿼리에서 반환된 열 수를 결정하는 SQL 삽입 UNION 공격

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. 쿼리의 결과는 응용 프로그램의 응답으로 반환되므로 UNION 공격을 사용하여 다른 테이블에서 데이터를 검색할 수 있습니다. 이러한 공격의 첫 번째 단계는 쿼리에서 반환되는 열의 수를 결정하는 것입니다. 그런 다음 후속 실습에서 이 기술을 사용하여 전체 공격을 구성합니다.

랩을 해결하려면 null 값을 포함하는 추가 행을 반환하는 SQL 주입 UNION 공격을 수행하여 쿼리에서 반환하는 열 수를 확인합니다.

## Solution

제품 범주 필터에 Union SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2003%20-%201.png)

<br>

category 파라미터에 취약점 확인
```
' union select null --
' union select null,null --
' union select null,null,null --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2003%20-%202.png)

<br>

기존의 에러메세지가 뜨지 않음, 컬럼의 갯수는 3개임을 추측할 수 있다.

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2003%20-%203.png)