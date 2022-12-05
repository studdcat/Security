# Cross Site Tracing - XST

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=is_king&logNo=221620641940

https://guleum-zone.tistory.com/78

![](../img/TRACE%20%EB%A9%94%EC%86%8C%EB%93%9C.png)

HTTP TRACE 메소드를 지원하는 웹 서버를 대상으로 TRACE 요청을 보내서 사용자의 중요한 쿠키 값을 탈취하는 공격이다.

TRACE 메소드란? 관리 및 디버그 목적으로 사용되는 메소드이다. 이 메소드를 사용하여 웹 서버에 요청을 보내게 되면 서버는 요청받은 메시지를 body 영역에 그대로 담아 보낸다.

<br>

nmap 을 이용해 열려 있는 포트를 확인 할 수 있다.
```
nmap 192.168.190.130 -p 80 -script http-methods
>>>
PORT   STATE SERVICE
80/tcp open  http
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT POST MOVE MKCOL PROPPATCH
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
```

HTTP 헤더에 TRACE 로 바꿔서 패킷을 통과시키면 페이지 이름으로 된 .php 파일을 다운받을 수 있다.

파일 안에는 요청 받은 패킷의 내용을 확인할 수 있게된다.

## 대응방안
1, 리소스 별 메서드를 제한하거나 사용자의 권한을 검증한다.
