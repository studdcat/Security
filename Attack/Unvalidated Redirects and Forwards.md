# Unvalidated Redirects and Forwards

https://rudgns99.tistory.com/8

https://ekwkqk12.tistory.com/16

https://i2sec.github.io/2017/03/30/owasp_top_10_forward.html

<br>

### -- 2013 OWASP TOP 10 --

<br>

Redirect와 forward 취약점은 외부로부터 받은 문자열을 URL 주소로 사용하여 자동으로 연결할 때 유효성 검증을 하지 않는 경우에 발생한다.
유효성 검증이 되지 않은 페이지에 자동으로 이동될 시 Redirect의 경우에는 공격자가 미리 설정한 악의적인 서버로 접속되어 피싱이나 악성 코드 실행 등의 피해가 발생한다.

```
http://www.naver.com/login?url=
>>>
http://www.naver.com/login?url=hack.com
```

## 대응방안
1. 입력 값 검증 & 화이트리스트 방식

   타 사이트로의 자동전환에 사용할 URL과 도메인들의 화이트 리스트를 작성한 다음 그중에서 선택함으로써 악의적인 사이트 접근을 차단하고 매개변수에 포함된 값이 유효한지, 그 사용자 권한에 맞는 허용된 페이지인지 검증한다.