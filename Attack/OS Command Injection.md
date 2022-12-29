# 📍 OS Command Injection

#### -- 2021 OWASP TOP 10 --
A03: Injection (인젝션)
SQL, NoSQL, OS Command, ORM(Object Relational Mapping), LDAP, EL(Expression Language) 또는 OGNL(Object Graph Navigation Library) 인젝션 취약점은 신뢰할 수 없는 데이터가 명령어나 쿼리문의 일부분으로써, 인터프리터로 보내질 때 취약점이 발생합니다.

<br>

다양한 웹 애플리케이션 제작용 언어는 시스템에 내장되어있는 프로그램들을 호출할 수 있는 함수를 지원한다. 시스템 함수를 사용하면 이미 설치된 소프트웨어들을 쉽게 이용할 수 있다는 장점이 있다. 그러나 함수의 인자를 셸의 명령어로 전달한다는 점에서 치명적인 취약점으로 이어지기도 한다.

Command Injection 은 웹 애플리케이션에서 시스템 명령을 사용할 때, 세미콜론 혹은 &, |, ; 등을 사용하여 하나의 Command를 Injection 하여 두 개의 명령어가 실행되게 하는 공격 입니다.

서버자체의 콘솔 명령어를 실행시킬 수 있기 때문에 공격이 성공한다면 매우 큰 피해가 발생할 수 있습니다.

Command Injection 공격이란 사용자가 입력하는 인자 값을 조작해 OS 명령을 실행하는 공격기법이다. 웹을 통해 시스템 명령어를 실행하게 되며, 특정 명령어 실행에 성공하면 작게는 파일정보 유출 크게는 시스템 장악까지 가능하다. Command Injection이 발생할 경우 현재 Command를 실행시키는 웹 어플리케이션의 권한만큼 해당 서버에서 권한을 획득할 수 있다.

<br>

## ⚔ Offensive techniques

```
| id
| ls
| whoami
| cat /etc/passwd
| cat /etc/shadow
& id
; id
| ping -c 10 8.8.8.8
; system('id')
%0Acat%20/etc/passwd
```

<br>

## 🔒 Denfensive techniques

OS command를 아예 사용하지 않는 것

입력 값 필터링 & 화이트리스트 검사

htmlspecialchars는 함수를 이용하여 특수문자를 UTF-8로 인코딩한다.

<br>

## Reference

https://portswigger.net/web-security/os-command-injection

https://noirstar.tistory.com/267

https://velog.io/@jjewqm/Command-Injection

https://hackersonlineclub.com/command-injection-cheatsheet/