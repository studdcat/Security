# Command Injection_01

https://portswigger.net/web-security/os-command-injection/lab-simple

https://www.youtube.com/watch?time_continue=339&v=GDUadTiXXVk&feature=emb_title

## Question
이 Lab에는 제품 재고 검사기 의 OS Command Injection 취약점이 포함되어 있습니다.

응용 프로그램은 사용자가 제공한 제품 및 매장 ID가 포함된 셸 명령을 실행하고 명령의 Command 출력을 응답으로 반환합니다.

실습을 해결하려면 whoami명령을 실행하여 현재 사용자의 이름을 확인합니다.

## Solution
1. Burp Suite를 사용하여 stock level을 확인하는 요청을 가로채고 수정합니다.
2. 매개변수를 수정하여 *storeID*값을 지정합니다 *1|whoami*
3. 응답에 현재 사용자의 이름이 포함되어 있는지 확인합니다.

## Process
재고 검사기(stock level)를 proxy 했다.

![](../img/Command%20Injection_01_01.png)

productId storeId 두개의 파라미터 값이 보였다.

![](../img/Command%20Injection_01_02.png)

productId storeId 중에 produtId에 Command Injection 공격 구문을 넣어 봤다.

![](../img/Command%20Injection_01_03.png)

공격이 잘 성공된 모습이다.

![](../img/Command%20Injection_01_04.png)