# SSI - Server-Side Includes

HTML 동적 콘텐츠를 제공하는 데 사용되는 웹 응용 프로그램에 있는 지시어로 동적인 내용을 추가하기 위해 만들어진 기능으로 주로 방문자 수 세거나 홈페이지 로고 수정  등 간단한 기능 추가할 때 사용한다. 

또한 '.shtml' 확장자 파일을 사용한다.

애플리케이션이 취약한지 확인하는 방법 중 하나는 ***.stm, .shtm, .shtml***인 페이지가 있는지 확인하는 방법이다.

공격자는 암호 파일과 같은 중요한 정보에 액세스하고 셸 명령을 실행할 수 있습니다. SSI 지시문은 입력 필드에 삽입되어 웹 서버로 전송됩니다. 웹 서버는 페이지를 제공하기 전에 지시문을 구문 분석하고 실행합니다. 그런 다음 다음에 사용자 브라우저에 페이지가 로드될 때 공격 결과를 볼 수 있습니다.

<br>

## ⚔ Offensive techniques

SSI 지시어를 이용하여 공격구문을 실행할 수 있다.

```html
<!--#exec -->
<!--#exec cmd="ls" -->
<!--#exec cmd="cat /etc/passwd" -->
```

<br>

## ✈ Denfensive techniques

### 입력 값 필터링

" < ! # = / . " - > and [a-zA-Z0-9] "

htmlspecialchars 함수

<br>

## Reference

https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection