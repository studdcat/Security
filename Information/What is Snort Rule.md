# What is Snort Rule

## Snort Rule?

IP 네트워크에서 프로토콜 분석, 콘텐츠 검색 및 비교 작업 등 실시간 트래픽 분석과 패킷 로깅 작업을 수행하여 다양한 공격과 스캔을 탐지하는 방법이다.

<br>

### Snort Rule 구조

|Rule Header|Rule Option|
|:---:|:---:|
|Action, Protocol, SrcIp, SrcPort -> DstIp, DstPort|Option|

<br>

### Action 유형

|명령어|내용|
|:---:|:---:|
|alert|경고 발생 및 로그 기록|
|log|로그 기록|
|pass|패킷 무시|
|drop|패킷 차단 및 로그 기록 (IPS 기능으로 사용. 단, 인라인 구조가 되어야 한다)|
|reject|패킷 차단 및 로그 기록 (TCP - TCP RST 응답, UDP - ICMP Unreachable 응답)|
|sdrop|패킷 차단 및 로그 기록 없음|

<br>

### Action 유형

|명령어|내용|
|:---:|:---:|
|tcp|TCO 탐지|
|udp|UDP 탐지|
|ip|IP 전체 탐지|
|icmp|ICMP 메시지 탐지|
|any|전체|

<br>

## Reference 

https://m.blog.naver.com/on21life/221387957157

https://latte-is-horse.tistory.com/21