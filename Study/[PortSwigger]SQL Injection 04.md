# [PortSwigger]SQL Injection 04

https://portswigger.net/web-security/all-labs

## LAB
SQL 주입 UNION 공격, 텍스트가 포함된 열 찾기

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. 쿼리의 결과는 응용 프로그램의 응답으로 반환되므로 UNION 공격을 사용하여 다른 테이블에서 데이터를 검색할 수 있습니다. 이러한 공격을 구성하려면 먼저 쿼리에서 반환된 열 수를 결정해야 합니다. 이전 실습 에서 배운 기술을 사용하여 이 작업을 수행할 수 있습니다 . 다음 단계는 문자열 데이터와 호환되는 열을 식별하는 것입니다.

실험실에서는 쿼리 결과 내에 표시해야 하는 임의의 값을 제공합니다. 실습을 해결하려면 제공된 값이 포함된 추가 행을 반환하는 SQL 주입 UNION 공격을 수행합니다. 이 기술은 문자열 데이터와 호환되는 열을 결정하는 데 도움이 됩니다.

## Solution

제품 범주 필터에 Union SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2004%20-%201.png)

<br>

category 파라미터에 취약점 확인
```
' union select '3We2S5',null,null --
' union select null,'3We2S5',null --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2004%20-%202.png)

<br>

Union SQL Injection 공격이 성공한 모습

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2004%20-%203.png)