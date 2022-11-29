# What is HTTP

https://noahlogs.tistory.com/34

https://developer.mozilla.org/ko/docs/Web/HTTP/Messages#%EB%B3%B8%EB%AC%B8

https://ko.wikipedia.org/wiki/HTTP

https://namu.wiki/w/%ED%8C%80%20%EB%B2%84%EB%84%88%EC%8A%A4%EB%A6%AC

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