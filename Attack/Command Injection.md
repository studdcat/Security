# Command Injection

https://portswigger.net/web-security/os-command-injection

https://hackersonlineclub.com/command-injection-cheatsheet/ - cheatsheet

https://noirstar.tistory.com/267

https://velog.io/@jjewqm/Command-Injection

### -- 2021 OWASP TOP 10 --
A03: Injection (인젝션)
SQL, NoSQL, OS 명령, ORM(Object Relational Mapping), LDAP, EL(Expression Language) 또는 OGNL(Object Graph Navigation Library) 인젝션 취약점은 신뢰할 수 없는 데이터가 명령어나 쿼리문의 일부분으로써, 인터프리터로 보내질 때 취약점이 발생합니다.

<br>

# 개요
Command Injection 은 웹 애플리케이션에서 시스템 명령을 사용할 때, 세미콜론 혹은 &, | 등을 사용하여 하나의 Command를 Injection 하여 두 개의 명령어가 실행되게 하는 공격 입니다.

서버자체의 콘솔 명령어를 실행시킬 수 있기 때문에 공격이 성공한다면 매우 큰 피해가 발생할 수 있습니다.

Command Injection 공격이란 사용자가 입력하는 인자 값을 조작해 OS 명령을 실행하는 공격기법이다. 웹을 통해 시스템 명령어를 실행하게 되며, 특정 명령어 실행에 성공하면 작게는 파일정보 유출 크게는 시스템 장악까지 가능하다. Command Injection이 발생할 경우 현재 Command를 실행시키는 웹 어플리케이션의 권한만큼 해당 서버에서 권한을 획득할 수 있다.

<br>

```
www.naver.com | etc/passwd
```

이처럼 주소를 적는 쿼리문에 명렁어를 | 뒤에 삽입 하면

```
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

위와 같이 명령문이 실행된다.

<br>

## 대응방안
1. OS command를 아예 사용하지 않는 것
2. 입력 값 필터링 & 화이트리스트 검사
