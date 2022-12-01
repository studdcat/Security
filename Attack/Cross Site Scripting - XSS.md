# Cross Site Scripting - XSS

https://namu.wiki/w/XSS

https://nordvpn.com/ko/blog/xss-attack/

https://4rgos.tistory.com/1

SQL Injection 과 함께 가장 기초적인 취약점 공격 방법이다.

보통 게시판이나 메일 등에 자바 스크립트와 같은 스크립트 코드를 넣어 쿠키, 세션을 탈취하거나 피싱 사이트 등으로 유도할 수 있다.

공격 방법에 따라 Reflected XSS, Stored XSS, DOM Based XSS 로 나뉜다.

## Reflected XSS

![](../img/)

가장 일반적인 유형의 XSS 이며 사용자에게 입력받은 값을 되돌려줄 때 발생합니다.

Reflected XSS 는 사용자가 직접 스크립트를 수행하도록 유도 하기 때문에 1회성 공격이라고 할수 있다. 오류메세지 등을 사용자에게 화면애 표시될 수 있다.

이 뿐만아니라 내용 난독화 스크립트 난독화등 우회 공격 구문은 많이 존재한다.

![](../img/)

## Stored XSS
영구적 XSS 공격이라고도 하며 공격자는 게시판에 스크립트를 삽입하는 등 지속적으로 피해를 입히는 공격 유형이다.

삽입된 스크립트는 데이터베이스에 저장하게 되고 악성 스크립트가 존재하는 게시판 열람 시 쿠키를 탈취당하거나 다른 사이트로 리다이렉션 되는 등 데이터베이스에 저장되어 지속적으로 공격을 실시하기 때문에 많은 피해자가 발생될 수 있다.

Stored XSS 공격이 제일 많이 발생하는 곳은 게시판이며 사용자가 링크를 클릭하게 유인할 필요 없이 접속만을 기다리면 되기 때문이다.

## DOM Based XSS 
웹페이지를 여는 즉시 생성 되는 DOM(Document Object Model)은 사용자가 서버와 상호 작용하지 않고도 페이지의 모든 콘텐츠에 액세스할 수 있도록 돕는 프로그래밍 인터페이스이다.

DOM 기반 XSS 공격은 피해자의 브라우저에 초점을 맞춘 것이 특징인 공격이다.

DOM 기반 XSS는 웹사이트의 코드를 조사하지 않고는 취약점을 발견할 수 없다. 이 때문에 전문 기술 지식을 갖추지 않은 이상 DOM 기반 XSS 공격에 당하기 쉽다. 

<br><br>

Example 1.

공격 구문
```
<script>alert("1")</script>
<a href="javascript:alert('XSS')">XSS</a>
<img src="#" onerror="alert('XSS')">
<ruby oncopy="alert('XSS')">XSS</ruby>
```

## XSS 위험성
쿠키 정보 및 세션 ID 획득

게시판에 공격을 수행함으로써 사용자의 쿠키를 탈취할 수 있다.

<br>

시스템 관리자 권한 획득

아직 패치되는 않은 취약점에 대한 공격 코드를 실행하게 하여 시스템을 통제할 수 있다.

<br>

악성코드 다운로드

XSS 직접적으로 다운로드를 받게할 수 없지만 URL을 클릭하도록 유도하여 그 사이트에서 악성코드르 다운로드 받게 할수 있다.

<br>

거짓 페이지 노출

img 태그를 이용하여 전혀 다른 페이지를 이용하여 정보들을 탈취할 수 있게한다.

## 대응방안
안타깝게도 XSS 는 IPS ID 방화벽 등으로 방지할 수 없다. 단순히 문자를 필터링하는 방법으로만 방지할 수 있다.

입력 값 검증 및 화이트리스트 방식 적용