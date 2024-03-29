# Q&A

https://an-onymous.tistory.com/entry/%F0%9F%94%90-%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EA%B0%9C%EB%B0%9C-%EB%B3%B4%EC%95%88-%EA%B5%AC%EC%B6%95-9-API-%EC%98%A4%EC%9A%A9

https://www.mois.go.kr/cmm/fms/FileDown.do?atchFileId=FILE_00105617Cv76vCd&fileSn=4

🐌

<p>
1. API 오용이란?
</p>

API 오용이란? 소프트웨어 구현 단계에서 API를 잘못 사용하거나 보안에 **취약한 API를** 사용하는 것을 말한다.

대표적으로 API 오용으로 인한 보안약점이다.
1. DNS Lookup에 의존한 보안 결정

    **도메인명 확인(DNS lookup)으로** 보안결정을 수행할 때 악의적으로 변조된 
    DNS 정보로 예기치 않은 보안위협에 노출되는 보안약점

2. 취약한 API 사용
   **취약한 함수를** 사용해서 예기치 않은 보안위협에 노출되는 보안약점

---

API : 라이브러리가 제공하는 여러 함수를 이용해서 프로그램을 작성할 때 해당 함수의 내부 구조는 알 필요없이 단순히 API 명세서에 정의된 값을 입력하면 반환되는 결과를 이용할 수 있도록 만든 매개체이다.

<br><br>

https://noahlogs.tistory.com/35

<p>
2. GET, POST 방식
   
GET 과 POST 는 HTTP 메서드로 클라이언트에서 서버로 무언가 요청할 때 사용된다.

패킷이 전송될 때는 Header 영역과 Body 영역으로 나뉘어진다. 어떠한 메서드를 이용했는지에 따라 사용의 유무도 달리지게 된다.

<br><br>

<p>
3. 피싱사이트 인터넷 상으로 올리는법?

<br><br>

<p>
4. 검증되지 않은 리다이렉션과 포워드 취약점을 발견했는데 이게 왜 위험이 될까?

취약점의 개요는 다른 URL 로 리다이렉션이 가능하게 해 악성사이트에 접근이 가능하게 하는 것이다.

근데 왜 이게? 문제가 될까? 나는 처음에는 단순히 그냥 이동이 되니깐 취약하다라고 생각을 했는데 뒤이어 질문을 해주셨다.

그건 우리가 버프로 잡아서 임의로 바꾼건데 사이트 사용자들에게는 어떻게 피해를 줄껀데요? 라고 하셔서 말문이 막혔다.

이후 이유도 제시하고 피드백도 들은 결과 정답은 이러했다.

우리는 발견한 이 취약점을 다른 방법을 통해서 사용자가 접근하게 만들어야한다. 예를 들어 이메일을 보내 이 취약점으로 들어오게끔 하던지 다른 공격기법을 이용하여 이 취약점으로 접근하게 해야한다는 것이다.

좀 더 쉬운 예시로 우리는 취약점을 통해 벌집을 만들었고 이 자체로는 문제는 안되지만 다른 방법으로 이 벌집을 건들이게 끔 하는게 방법인거다.

이 과정을 통해 나무가 아닌 숲을 볼수 있는 시야가 생긴 것 같다.

<br><br>

<p>
5. 내 브라우저에서 네이버로 가기까지의 과정

내가 알아볼 것은 네트워크의 흐름, OSI 7계층, IP Header 에 대해 알아 보겠다.

네트워크 흐름 : 만약 내가 네이버를 URL 창에 검색한다고 가정하자 검색하는 순간 순식간에 네이버로 접속되지만 실상은 매우 복잡하고 많은 과정이 일어난다.

내 브라우저 > DNS > 내 브라우저 > 네이버 > 내브라우저

크게 이런 순서로 내 화면에 나타나게 된다.

여기서 질문 OSI 7계층도 비슷하게 전송이 되는 건데 이거랑 뭐가 달라?

결론부터 말하자면 OSI 7계층의 방식을 이용해서 네트워크 흐름을 하는 것이다. 네트워크 흐름이 범위가 더 크다고 생각하면된다.

IP Header는 뭐야? OSI 7계층 보다 더 안쪽을 보면은 IP 패킷을 주고 받는다 그때 IP 패킷 앞에 붙는게 Header이다 이런식으로 매우 복잡하고 많은 과정이 거의 1초안으로 다이루어 진다고 생각하면 된다.

<br><br>

<p>
6. nmap 사용시 추가사항
   
nmap -sT [주소] 사용 시
http: ~~/asdas/~ 여기까지 하는게 아니라 웹 루트 디렉토리 까지만

왜냐 웹서버 전체를 스캔해야하는거니깐 웹루트 디렉토리에서 스캔하는게 맞다. 최고 위에서 실행하는게 상식선으로 맞다.

정확히는 디렉토리가 아니라고 하셨다. 그럼 뭘까?

<br><br>

https://stackoverflow.com/questions/19938048/are-server-500-errors-a-security-issue

https://namu.wiki/w/500%20Internal%20Server%20Error

<p>
7. 응답 코드 500에 관하여
404와 403의 차이를 가지고 서버의 구조를 알수 있다. 이것은 익히 들었다. 하지만 500? 이것은 그냥 서버 쪽 오류구나 하고 흘려보냈는데 아니었다.

사이트 자체의 에러로는 1. 서버 스크립트의 오류 2. 서버 사용량의 폭주로 일시적인 오류 이 두 가지가 에러의 원인이다. *주로 1번이 많이 발생한다.*

예를들어 SQLI 공격을하는데 도움을 줄수있다. DB 쪽을 공격을 하는데 DB에 맞지 않는 스크립트 구문을 썼던지 이런식으로 공격시에 정보가 도움이 되기 때문에 왠만하면 500에러 페이지는 노출이 되지 않는 것이좋다.

500의 에러는 취약점이 존재하거나 하지않거나를 알수있는 정보가 된다.

500 노출을 통해 공격자가 유효한 요청 시도와 잘못된 요청 시도를 구분할 수 있음을 나타낸다

Timebased Blind Sql Injection 시도 시 확인가능 서버 요청시간이 길면은 에러페이지 뱉어내니깐