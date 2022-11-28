# DNS Lookup에 의존한 보안 결정

https://www.mois.go.kr/cmm/fms/FileDown.do?atchFileId=FILE_00105617Cv76vCd&fileSn=4

https://it-license.tistory.com/93

DNS Lookup 명령어를 통해 얻은 도메인명을 가지고 유효성을 판단하는 경우 DNS 위변조시에는
잘못된 도메인명에 의해서 트래픽이 공격자를 경유하게 될 수도 있고, 공격자가 마치 동일 도메인에
속한 서버인 것처럼 위장할 수 있다

공격자가 DNS 엔트리를 속일 수 있으므로 도메인명에 의존에서 보안결정(인증 및 접근 통제 등)을 
하지 않아야 한다. 만약, 로컬 DNS 서버의 캐시가 공격자에 의해 오염된 상황이라면, 사용자와 
특정 서버 간의 네트워크 트래픽이 공격자를 경유하도록 할 수도 있다. 또한, 공격자가 마치 동일 
도메인에 속한 서버인 것처럼 위장할 수도 있다

## 대응방안
보안결정에서 도메인명을 이용한 DNS lookup을 하지 않도록 한다.

```java
 public void doGet(HttpServletRequest req, HttpServletResponse res) 
    throws ServletException, IOException 
    {
    boolean trusted = false;
    String ip = req.getRemoteAddr();
    InetAddress addr = InetAddress.getByName(ip);
    // 도메인은 공격자에 의해 실행되는 서버의 DNS가 변경될 수 있으므로 안전하지 않다.
    if (addr.getCanonicalHostName().endsWith("trustme.com")) {
        do_something_for_Trust_System();
    }
```