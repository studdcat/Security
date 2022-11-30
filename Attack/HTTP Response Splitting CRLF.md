# HTTP Response Splitting CRLF Injection

https://owasp.org/www-community/attacks/HTTP_Response_Splitting

https://m.blog.naver.com/skinfosec2000/220694143144

https://cordingdiary.tistory.com/50

HTTP Rquest에 있는 파라미터가 HTTP Response의 응답헤더로 다시 전달되는 경우 파리미터 내 개행문자 CR(%0D, \r) 또는 LF(%0A, \n)가 존재하면 HTTP 응답이 분리될 수 있다.
HTTP 응답분할 공격은 응답 메세지에 악의적인 코드를 주입함으로써 XSS 및 캐시를 훼손할 수 있다.

HTTP 헤더는 일반적으로 웹 브라우저가 서버에 요청하고(Request) 웹 브라우저 표기를 위해 서버로 부터 다시 응답(Response) 받아 해석한다.

Example 1.

```
/board_view.php?num=5 **%0D%0A** [~~~]
>>>
< ~~~ 
>
```

Example 2.

total_money 에 %0d%0a를 삽입하였다 
```
amount_1=1&milage_1=2910&uid=216&total_money=97000%0d%0a&total_milage=2910&total_count=2&x=78&y=8
>>>
<input type="hidden" name="total_money" value="97000
">
```

Example 3.

공격구문
```
/main/main.asp?num=5 HTTP/1.1
>>>
/main/main.asp?num=5%0d%0aContentLength:%200%0d%0d%0a%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2019%0d%0a%0d%0a<html>Attack</html> HTTP/1.1
```

## 대응방안
1.HTTP 헤더에 입력되는 값에 대하여 개행문자 CR, LF를 필터링한다.
```
String test = test.replaceAll("\r,"").replaceAll("\n,""")
```

<br><br>

---
#Get, Post 둘다 되나? http 응답이 왜야하니깐 Get만 될 것같기도 함