# π HTML Injection

μ·¨μ½ν λ§€κ°λ³μμ μμμ μΈ HTML μ½λλ₯Ό μ½μνμ¬ μ¬μ©μκ° μλνμ§ μμ νμ΄μ§λ₯Ό λ³΄μ¬μ£Όκ±°λ μμ± μ¬μ΄νΈλ‘ μ°κ²° μν¬ μ μμ΅λλ€.

GET, POST, Stored 3κ°μ§μ κ³΅κ²© λ°©λ²μ΄ μμ΅λλ€.

<br>

### GET(Reflected)

GET λ°©μμΌλ‘ κ°μ ν€λλ‘ ν΅ν΄ μ λ¬ν  λ λ°μν©λλ€.

URL λ€μ μ½λλ₯Ό μ½μνκΈ° λλ¬Έμ λ°μ΄ν°μμ μ νμ μλλ€.

<br>

### POST(Reflected)

POST λ°©μμΌλ‘ κ°μ λ°λλ‘ ν΅ν΄ μ λ¬ν  λ λ°μν©λλ€.

λ°λλ‘ κ°μ μ λ¬νκΈ° λλ¬Έμ λ§μ λ°μ΄ν°μμ λ³΄λΌ μ μμ΅λλ€.

<br>

### Stored

μμμ μΈ HTML μ½λλ₯Ό DBμ μ μ₯νμ¬ μ¬μ©μ PCμμ HTML νκ·Έκ° μ€νλκ²ν©λλ€.

λ€μμ νΌν΄μκ° λ°μν  μ μμ΅λλ€.

<br>

## β Offensive techniques

``` html
<h1>

<h1>Success</h1>

<img src="/images/~~~">

<img src=">

<form action="<textarea>

<a href="https://www.naver.com">Click</a>

<base href="https://www.naver.com">

<meta http-equiv="refresh" content="0;url=https://www.naver.com">
```

<br>

## π Denfensive techniques

htmlspecialcharsλ νΉμλ¬Έμ(&, ", ', <, >)λ₯Ό UTF-8λ‘ λ°ννλ€.

htmlspecialcharsλ ν¨μλ₯Ό μ΄μ©νμ¬ νΉμλ¬Έμλ₯Ό UTF-8λ‘ μΈμ½λ©νλ€.

<br>

## Reference

https://www.invicti.com/learn/html-injection/