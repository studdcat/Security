# SYN Flooding

## SYN Flooding?

SYN Flooding 공격이란 DDos 공격의 한 종류이며, TCP의 연결 과정인 3-way-handshake에서 취약점을 이용한 공격기법이다.

<br>

### 3-way-handshake?

TCP 방식의 특징은 연결형 방식이다. 그 때 서로 연결해주는 방식이 3-way-handshake 이다. 3-way-handshake란 SYN과 ACK을 이용하여 서로의 연결의 신뢰를 보장한다.

(1) [Client] SYN -> [Server]

(2) [Client] <- SYN, ACK+1 [Server]

(3) [Client] ACK+1 -> [Server]

이와 같은 과정을 통해 연결한다.

<br>

## 🚩 Offensive techniques

SYN Flooding은 2번쨰 과정인 Server가 SYN, ACK을 보냈을 때 Client에게 다시 ACK을 받기 위해 메모리를 할당하고 있는 취약점을 이용한다.

Client가 ACK을 보내지 않고 많은 SYN만 보낸다면 Server는 엄청난 메모리를 소비하고 있을 것이다. 이점을 이용해 서버에 메모리 공간이 부족하게 만들어 서버를 과부하시키는 공격기법이다.

<br>

## 🛡 Denfensive techniques

### SYN Cookie

방화벽 단에서 SYN을 먼저 받고 SYN Cookie를 포함한 SYN, ACK을 보내는 방법이다. 일정시간 동안 정상적인 응답이 돌아오지 않으면 방화벽에서 차단을 시키고 정상적인 통신을 하게한다.

(1) [Client] SYN -> [F/W] [Server]

(2) [Client] <- SYN, ACK+1 [F/W] [Server]

(3) [Client] ACK+1 -> [F/W] [Server]

(4) [Client] SYN -> [Server]

(5) [Client] <- SYN, ACK+1 [Server]

(6) [Client] ACK+1 ->  [Server]

위의 과정은 정상적인 통신과정을 표현한다.

(1) [Client] SYN -> [F/W] [Server]

(2) [Client] <- SYN, ACK+1 [F/W] [Server]

(3) [Client] SYN -> [F/W] [Server]

(4) [Client] <- SYN, ACK+1 [F/W] [Server]

(5) [Client] SYN -> [F/W] [Server]

(6) [Client] <- SYN, ACK+1 [F/W] [Server]

위의 과정은 비정상적인 통신과정을 표현한다.

<br>

### SYN PROXY

방화벽 단에서 정상적인 3-way-handshake과정이 이루어지면, 그 연결을 다시 서버에게 재현시켜주는 방식입니다. 3-way-handshake 연결이 이루어지지 않은 경우에는 방화벽에서 차단한다.

(1) [Client] SYN -> [F/W] [Server]

(2) [Client] <- SYN, ACK+1 [F/W] [Server]

(3) [Client] ACK+1 -> [F/W] [Server]

(4) [Client] [F/W] SYN -> [Server]

(5) [Client] [F/W] <- SYN, ACK+1 [Server]

(6) [Client] [F/W] ACK+1 ->  [Server]

위의 과정은 정상적인 통신과정을 표현한다.

비정상적인 통신과정은 SYN Cookie와 동일하다.

<br>

## Reference

https://sata.kr/entry/DOSDDOS-SYN-Flooding-%EA%B3%B5%EA%B2%A9%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90