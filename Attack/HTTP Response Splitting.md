# HTTP Response Splitting

https://owasp.org/www-community/attacks/HTTP_Response_Splitting

https://m.blog.naver.com/skinfosec2000/220694143144

HTTP Rquest에 있는 파라미터가 HTTP Response의 응답헤더로 다시 전달되는 경우 파리미터 내 개행문자 CR(%0D) 또는 LF(%0A)가 존재하면 HTTP 응답이 분리될 수 있다.
HTTP 응답분할 공격은 응답 메세지에 악의적인 코드를 주입함으로써 XSS 및 캐시를 훼손할 수 있다.

HTTP 헤더는 일반적으로 웹 브라우저가 서버에 요청하고(Request) 웹 브라우저 표기를 위해 서버로 부터 다시 응답(Response) 받아 해석한다.

Example 1.
```
/board_view.php?num=5%0D%0A [~~~]
```

## 대응방안
1. HTTP 헤더에 입력되는 값에 대하여 개행문자 CR, LF를 필터링한다.