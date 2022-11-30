# SQL Injection
https://blog.naver.com/skinfosec2000/220482240245

https://ssunws.tistory.com/44


https://noirstar.tistory.com/264

https://pentestmonkey.net/category/cheat-sheet/sql-injection - cheat sheet

<br>

![](../img/SQL%20Injection%20-%20process.png)

### -- 2021 OWASP TOP 10 --
A03: Injection (인젝션)
SQL, NoSQL, OS 명령, ORM(Object Relational Mapping), LDAP, EL(Expression Language) 또는 OGNL(Object Graph Navigation Library) 인젝션 취약점은 신뢰할 수 없는 데이터가 명령어나 쿼리문의 일부분으로써, 인터프리터로 보내질 때 취약점이 발생한다.

<br>

SQL Injection 이란 악의적인 사용자가 보안상의 취약점을 이용하여, 임의의 SQL 문을 주입하고 실행되게 하여 데이터베이스가 비정상적인 동작을 하도록 조작하는 행위이다.

<br>

## Error based SQL Injection
SQL 공격 기법은 여러 가지가 있는데 논리적 에러를 이용한 SQL Injection은 가장 많이 쓰이고, 대중적인 공격 기법이다.

![](../img/SQL%20Injection%20-%20process%20-%202.png)

위의 사진에서 보이는 쿼리문은 일반적으로 로그인 시 많이 사용되는 SQL 구문이다. 해당 구문에서 입력값에 대한 검증이 없음을 확인하고, 악의적인 사용자가 임의의 SQL 구문을 주입하였다. 주입된 내용은 ‘ OR 1=1 -- 로  WHERE 절에 있는 싱글쿼터를 닫아주기 위한 싱글쿼터와 OR 1=1 라는 구문을 이용해 WHERE 절을 모두 참으로 만들고, -- 를 넣어줌으로 뒤의 구문을 모두 주석 처리 해주었다.

매우 간단한 구문이지만, 결론적으로 Users 테이블에 있는 모든 정보를 조회하게 됨으로 써 가장 먼저 만들어진 계정으로 로그인에 성공하게 된다. 보통은 관리자 계정을 맨 처음 만들기 때문에 관리자 계정에 로그인 할 수 있게 된다. 관리자 계정을 탈취한 악의적인 사용자는 관리자의 권한을 이용해 또 다른 2차피해를 발생 시킬 수 있게 된다.

<br><br>

다른 예시로

```
SELECT * FROM member WHERE id = '[value1]' AND pw = '[value2]'

SELECT * FROM member WHERE id = '[value1]' AND pw = '' or 1=1 --'
```

다른 사용자의 id를 알고 있다는 가정하에 ***' or 1=1 --*** 구문을 이용해서 pw 없이 접근이 가능하다.

앞에 싱글쿼터는 다른 싱글쿼터(')로 닫아주고 주석(--)을 이용하고  or 1=1 은 참이 되어서 pw 없이 로그인이 가능하다.

id만 같다면 뒤에 오는 pw는 무조건 참이 되니깐 말이다.

---보통 처음에는 ' 를 하난 

<br>

### 공격구문

```
'
' or 1=1 --
' or 1=0 --
```

<br>

## Union SQL Injection
SQL의 Union 키워드를 이용하는 공격기법이다.
Union은 두 개의 쿼리문에 대한 결과를 합쳐서 하나의 테이블로 보여주는 키워드이다.

union injection을 하기 위해서는 두 가지의 조건이 필요하다.
두 테이블의 컬럼 수가 같아야하고, 데이터형이 같아야한다.

Example 1.

union injection의 공격흐름이다.

```
' and db_name() > 1 --
' union select null --
' union select null,null --
' union select null,null,null ... --
' union select @@version --
' union select table_name,null,null from infromation_schema.tables --
' union select column_name,null,null from infromation_schema.columns where = '[table_name]' --
' union select [column_name],null,null from [table_name] --
```

<br>

## Blind SQL Injection
### Boolean based SQL
Boolean based SQL은 데이터베이스로부터 특정한 값이나 데이터를 전달받지 않고 단순히 참과 거짓의 정보만 알 수 있을 때 사용한다.

Example 1.

```
[ID]’ and ASCII(SUBSTR(SELECT name From information_schema.tables WHERE table_type=’base table’ limit 0,1)1,1)) > 100 --
```
해당구문은 MySQL 에서 테이블 명을 조회하는 구문으로 limit 키워드를 통해 하나의 테이블만 조회하고, SUBSTR 함수로 첫 글자만, 그리고 마지막으로 ASCII 를 통해서 ascii 값으로 변환해준다. 

만약에 조회되는 테이블 명이 Users 라면 ‘U’ 자가 ascii 값으로 조회가 될 것이고, 뒤의 100 이라는 숫자 값과 비교를 하게 된다.  
거짓이면 로그인 실패가 될 것이고, 참이 될 때까지 뒤의 100이라는 숫자를 변경해 가면서 비교를 하면 된다.  

공격자는 이 프로세스를 자동화 스크립트를 통하여 단기간 내에 테이블 명을 알아 낼 수 있다.

### Time based SQL
Time based SQL도 단순히 참과 거짓으로만 정보를 알 수 있을 때 사용한다.

Example 1.

```
[]' OR (LENGTH(DATABASE()) = 1 AND SLEEP(3)) --
```

악의적인 사용자가 []’ OR (LENGTH(DATABASE())=1 AND SLEEP(2)) – 이라는 구문을 주입하였다. 여기서 LENGTH 함수는 문자열의 길이를 반환하고, DATABASE 함수는 데이터베이스의 이름을 반환한다.

주입된 구문에서, LENGTH(DATABASE()) = 1 가 참이면 SLEEP(2) 가 동작하고, 거짓이면 동작하지 않는다. 이를 통해서 숫자 1 부분을 조작하여 데이터베이스의 길이를 알아 낼 수 있다.

<br>

## 대응방안
### # 매개변수 바인딩 & 저장프로시저 & prepared statement
<br>

![](../img/SQL_query_processing_1.jpg)
<br><br>

prepared statement를 사용하는 경우엔는 효율을 높이기 위해 <strong>parse</strong> 과정을 최초 1번만 수행하고 이후에는 생략할 수 있다. <strong>parse</strong> 과정을 모두 거친 후에 생성된 결과는 메모리 어딘가에 저장 해두고 필요할 때마다 사용한다. 반복적으로 트리를 사용하기 위해서 자주 변경되는 부분을 변수로 선언해 두고 매번 다른 값을 바인딩하여 사용한다.
<br><br>
바인딩 데이터는 문법 처리과정에서 미리 선 수행되고 SQL 문법이 아닌 내부의 인터프리터나 컴파일 언어로 처리하기 때문에 문법적인 의미를 가질 수 없다. 따라서 바인딩 변수에 SQL공격를 할지라도 공격은 실패한다.
<br><br>
### # 화이트리스트
화이티리스트란 '안전'이 증명된 것만을 허용하는 것으로 '악의성'이 입증된 것을 차단하는 블랙리스트 보안과 상반되는 보안 방식 이다. 화이트리스트, 블랙리스트라는 용어 대신 'positive'와 'nagㄴative' 보안 방법으로 불려지기도 한다.
<br><br>

### # 입력 값 필터링
<br>

### # 최소한의 권한 사용
<br>

### # 오류 메시지 출력 제한