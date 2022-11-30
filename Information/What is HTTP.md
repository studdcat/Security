# What is HTTP

https://noahlogs.tistory.com/34

https://developer.mozilla.org/ko/docs/Web/HTTP/Messages#%EB%B3%B8%EB%AC%B8

https://ko.wikipedia.org/wiki/HTTP

https://namu.wiki/w/%ED%8C%80%20%EB%B2%84%EB%84%88%EC%8A%A4%EB%A6%AC

https://velog.io/@jkijki12/HTTP-Header-%EC%A0%95%EB%A6%AC

## HTTP 란?

HTTP(Hyper Text Transper Protocol)란? www 상에서 데이터를 주고 받기위한 **통신규약(프로토콜)이다.**

1989년 **팀 버너스리**가 www, URL, HTTP 등을 만들어 웹을 탄생 시켰다. 그 중 HTTP는 하이퍼텍스트들을 주고 받기 위한 통신규약으로 만들어 진 것이다.

HTTP는 클라이언트(사용자)와 서버 사이에 이루어지는 요청/응답(request/response) 프로토콜이다. **요청(requset)은** 클라이언트가 서버로 전달해서 서버의 액션이 일어나게끔 하는 메세지이고, **응답(response)은** 요청에 대한 서버의 답변으로 실제로 우리가 보이는 화면을 답변해준다.

HTTP는 문서들 뿐만 아니라 비디오, 음성 등 거의 모든 데이터들을 전송하는데 사용되고 있다.

## HTTP 메세지 구조
클라이언트와 서버 사이의 전달은 ASCII로 인코딩된 평문(ASCII) 메세지로 이루어진다.

|-- 메세지 구조 --|
|:---:|
|시작 줄(start line)|
|HTTP 헤더(HTTP header)|
|공백(empty)|
|바디(body)|

시작 줄(start line) : 실행되어야 할 요청, 또은 요청 수행에 대한 성공 또는 실패가 기록되어 있다. 이 줄은 항상 한 줄로 끝난다.

HTTP 헤더(HTTP header) : 옵션으로 HTTP 헤더 세트가 들어간다. 여기에는 요청에 대한 설명, 혹은 메시지 본문에 대한 설명이 들어간다.

공백(empty) : 요청에 대한 모든 메타 정보가 전송되었음을 알리는 빈 줄(blank line)이 삽입된다.

바디(body) : 요청과 관련된 내용(HTML 폼 콘텐츠 등)이 옵션으로 들어가거나, 응답과 관련된 문서(document)가 들어간다. 본문의 존재 유무 및 크기는 첫 줄과 HTTP 헤더에 명시된다.

HTTP 메시지의 시작 줄과 HTTP 헤더를 묶어서 요청 헤드(head)라고 부르며, 이와 반대로 HTTP 메시지의 페이로드는 *본문(body)*이라고 합니다.

<br>

 HTTP 메시지는 기본적으로 클라이언트가 요청하고 서버가 응답하는 구조이기 때문에 메시지는 요청이냐 응답이냐에 따라 각 메시지의 구성 내용이 달라 진다.

|/|requset(요청)|response(응답)|
|:---:|:---:|:---:|
|**시작 줄(start line)**|1. HTTP 메서드 (GET, POST ...)<br>2. 요청 URL<br>3. HTTP 버전|1. HTTP 메서드 (GET, POST ...)<br>2. 상태코드 (200, 404 ...)<br>3. 상태 텍스트 (Not Found ...) 
|**HTTP 헤더(HTTP header)**|1. request 헤더 (Host, User-Agent, Accept ...)<br>2. general 헤더 (Connection ... )L<br>3. entity 헤더 (Content-Type ... )|1. response 헤더 (Server, Set-Cookie, Age ...)<br>2. general 헤더 (Connection ... )L<br>3. entity 헤더 (Content-Type ... )|
|**공백(empty)**|메타 데이터 전송이 끝났음을 알리는 공백|메타 데이터 전송이 끝났음을 알리는 공백|
|**바디(body)**|서버에 전송하는 데이터|클라이언트에 전달하는 데이터

![](../img/HTTP%20메세지%20구조%20예시.png)

## HTTP 메서드
HTTP 메서드는 클라언트가 서버측에 요청의 정보 및 목적을 알리는 수단이다.

HTTP 요청 시에는 시작줄에 표시된다.

|메서드|설명|
|:---:|:---:|
|GET|리소스 요청|
|POST|서버의 내용 전송|
|HEAD|메세지 헤더 요청|
|PUT|리소스 전체 수정요청|
|DELETE|리소스제 요청|
|OPTIONS|서버에서 제공하는 메서드 목록 요청|
|TRACE|요청 리소스가 수신되는 경로를 보여줌 메세지 loop-back 테스트 요청| 

## HTTP 헤더 구조
HTTP 메시지 구조를 보면 HTTP 헤더가 들어가는데 요청/응답 헤더 , general 헤더, entity 헤더 로 구분된다.

너무 많은 관계로 중요한 헤더만 설명 하겠다.

### General Header (공통 헤더)
|헤더명|설명|예시|
|:---:|:---:|:---:|
|Date|HTTP 메세지 생성 일시|Wed, 30 Nov 2022 04:19:21 GMT
|Connection|close, Keep-Alive 있다.<br>close는 메세지 교환 후 TCP 연결 종료<br>Keep-Alive는 메세지 교환 후 TCP 연결 유지|Connection: close<br>Connection: Keep-Alive|

### Requset Header (요청 헤더)
|헤더명|설명|예시|
|:---:|:---:|:---:|
|Host|요청하는 자의 호스트명, 포트 번호를 포함하고 있다.|Host: 192.168.190.130|
|User-Agent|클라이언트의 소프트웨어 정보를 표현한다. os, 브라우저, 기타 버전 정보|Mozilla/5.0 (Windows NT 10.0; Win64; x64)|
|Accept|클라이언트가 원하는 미디어의 타입 및 우선순위를 표현한다.|text/html,application/xhtml+xml ...|
|Cookie|서버에 의해서 이전에 저장된 쿠키를 포함시키는 속성이다.|Cookie: user_id=3LEMQRTO6EBF4;|
|Referer|특정 페이지에서 링크를 클릭하여 요청하였을 경우 직전에 머물렀던 링크 주소||

### Response Header (응답 헤더)
|코드|메세지|설명|
|:---:|:---:|:---:|
|Server|서버 소프트웨어 정보|Microsoft-IIS/5.0|
|Content-Type|응답하는 내용의 타입과 문자 포맷을 표현한다.|text/html|
|Content-Length|응답하는 내용의 길이|88349|
|Set-Cookie|서버에서 사용자에게 세션 쿠키 정보를 전달한다.||

## 응답 코드
HTTP 상태코드는 응답 메시지 중에서도 시작 줄에 표기 된다. 

HTTP 상태코드는 요청에 대한 처리 결과를 알려 준다.

상황에 따라 상태코드는 3자리 숫자로 표현하는데 100 대 부터 500 대까지가 있다. 

클라이언트가 서버에 접속하여 어떠한 요청을 하면, 서버는 세 자리 수로 된 응답 코드와 함께 응답한다.

많은 관계로 중요한 코드만 설명 하겠다.

|코드|메세지|설명|
|:---:|:---:|:---:|
|1xx|Informational(정보)|정보 교환.|
|100|Continue|클라이언트로부터 일부 요청을 받았으니 나머지 요청 정보를 계속 보내주길 바람.|
|2xx|Success(성공)|	데이터 전송이 성공적으로 이루어졌거나, 이해되었거나, 수락되었음.|
|200|OK|오류 없이 전송 성공.|
|3xx|Redirection(방향 바꿈)|	자료의 위치가 바뀌었음.|
|300|Multiple Choices|최근에 옮겨진 데이터를 요청.|
|4xx|Client Error(클라이언트 오류)|클라이언트 측의 오류. 주소를 잘못 입력하였거나 요청이 잘못 되었음.|
|403.1|Forbidden|금지 (수행접근 금지). 수행시키지 못하도록 되어있는 디렉터리 내의 실행 파일을 수행하려고 하였음.|
|404|Not Found|문서를 찾을 수 없음. 서버가 요 청한 파일이나 스크립트를 찾지 못함.|
|5xx|Server Error(서버 오류)|서버 측의 오류로 올바른 요청을 처리할 수 없음.|
|500|Internal Server Error|서버 내부 오류|