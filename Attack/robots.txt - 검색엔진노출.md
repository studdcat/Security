# robots.txt - 검색엔진노출 취약점

https://isc9511.tistory.com/115

검색엔진에 의해 각종 정보들이 검색 되어 중요 정보들이 노출되는 취약점이다.

<br>


아래와 같이 robots.txt 안에 해킹에 필요한 정보들이 담겨 있을 수 있다.

```
User-agent: *
Disallow: /$
Allow : /admin
```

<br>

만약 robots.txt 가 없다면 크롤링 봇에 대한 접근이 없는거나 마찬가지이기 때문에 중요정보 탈취 가능성이 존재한다.

또한 크롤링 봇이 많은 요청 값을 보내기 때문에 서버 과부화가 일어날 수 있다.

<br>

robots.txt는 웹루트의 최상위에 위치해야한다.

```
http://example.com/robots.txt (o)
http://example.com/index/robots.txt (x)
```

<br><br>

robots.txt 설정방법

User-agent 와 Allow 또는 Disallow 로 작성된다.

User-agent 에는 접근을 제어할 로봇을 명시해준다.

Allow/Disallow 에는 허용 또는 제한할 URL을 명시해준다.

|robots.txt|내용|
|:---:|:---:|
|User-agent: *<br>Disallow: /<br>Allow : /$ |모든 로봇에 대해 접근을 제한한다.<br>웹 사이트 전체 접근 제한<br>첫 페이지만 접근허용|
|User-agent: *<br>Disallow: /search<br>Allow: /search/about|모든 로봇에 대해 접근을 제한한다.<br>search 디레터리 접근 제한<br>search/about 디렉터리 접근 허용|
|User-agent: * <br> Disallow/*/pulse <br> Disallow: / */tree/|모든 로봇에 대해 접근을 제한한다.<br>pulse 디레터리 접근 제한<br>tree 디레터리 접근 제한|

