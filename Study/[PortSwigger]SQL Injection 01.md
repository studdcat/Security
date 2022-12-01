# [PortSwigger]SQL Injection 01

https://portswigger.net/web-security/all-labs

## LAB
숨겨진 데이터 검색을 허용하는 WHERE 절의 SQL 삽입 취약성

## Qusetion
이 연구소에는 제품 범주 필터에 SQL 삽입 취약점이 포함되어 있습니다. 사용자가 카테고리를 선택하면 애플리케이션은 다음과 같은 SQL 쿼리를 수행합니다.

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

랩을 해결하려면 응용 프로그램이 ***모든 범주의 모든 제품***(출시 및 미출시)에 대한 세부 정보를 표시하도록 하는 SQL 주입 공격을 수행합니다.

## Solution

제품 범주 필터에 SQL Injection 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2001%20-%202.png)

<br>

category 파라미터에 취약점 확인

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2001%20-%203.png)

<br>


무조건 참이 되게 해서 모든 범주들이 확인됨.
```
' or 1=1 --
```

![](../img/Study%20Img/%5BPortSwigger%5DSQL%20Injection%2001%20-%204.png)