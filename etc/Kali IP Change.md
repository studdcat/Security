# IP 변경

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
address [변경할 IP 주소] ex) 192.168.130.0
netmask 255.255.255.0
gateway 192.168.130.1
broadcast 192.168.0.255

auto eth1
iface eth1 inet dhcp
```

게이트웨이 주소는 IP 주소와 같은 네트워크 주소에 할당해야 되나?