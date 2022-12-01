# GET POST

https://khj93.tistory.com/entry/GET-%EB%B0%A9%EC%8B%9D%EA%B3%BC-POST-%EB%B0%A9%EC%8B%9D-%EC%9D%B4%EB%9E%80-%EC%B0%A8%EC%9D%B4%EC%A0%90

https://brilliantdevelop.tistory.com/33

https://mommoo.tistory.com/60

GET 과 POST 는 HTTP 메서드로 클라이언트에서 서버로 무언가 요청할 때 사용된다.

패킷이 전송될 때는 Header 영역과 Body 영역으로 나뉘어진다. 어떠한 메서드를 이용했는지에 따라 사용의 유무도 달리지게 된다.

## GET 방식
GET은 서버에 요청할 때 정보를 body에 담지 않고 쿼리스트링을 통해 전달한다. 쿼리스트링이란 URL 끝에 ? 와 함께 이름과 값으로 쌍을 이루는 요청 파라미터를 쿼리 스트링이라 한다. 만약 요청 정보가 여러 개라면 &로 연결한다.

Example 1.

URL 예시

```
www.naver.com/login/id=guset&pw=1234
```

따라서 body에는 특별한 내용을 담을 필요가 없기 때문에 body부분은 빈 상태로 보내진다. 그러므로 헤더 중 boby의 데이터를 설명하는 Content-Type 헤더필드도 들어가지 않는다.

URL 에 정보를 넣어서 보내기 때문에 길이의 제한이 있다. HTTP/1.1 2048자 까지 가능하다.

그리고 GET은 불필요한 요청이 캐시될 수 있다. 변경이 적은 데이터를 매번 보낼 필요가 없기 때문에 요청을 캐시에 두고 동일한 요청이 발생 했을 때 캐시에 있는 데이터를 사용한다.
  
URL이 눈에 바로 보이기 때문에 비교적 POST보다는 보안에 취약하기 때문에 민감한 정보는 GET방식으로 보내지 않는다.

## POST 방식
리소스를 생성, 변경하기 위해 설계되었기 때문에 GET과 달리 전송해야할 데이터를 body부분에 담아서 전송한다. 

body을 통해 전송하기 때문에 길이에는 제한이 없어 대용량의 데이터를 보낼 때 유리하다. Content-Type 헤더필드도 같이 전송해줘야 한다.

GET 달리 캐시는 되지 않는다.

물론 GET 방식 보다는 보안에 좋다는 거지 POST 도 Burp 나 Fiddler 와 같은 툴로 패킷 내용을 확인할 수 다.

## GET 과 POST 의 차이점
**사용목적**의 차이점은 GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버의 리소스를 새로 생성하거나 업데이트할 때 사용한다.

GET은 SELECT에 가깝고 POST는 CREATE에 가깝다고 한다.

멱등성이란 연산을 여러번해도 결과가 달라지지 않는 성질을 말하는 건데 GET은 멱등성이고 POST는 멱등성이 아닌다.