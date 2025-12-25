[Pachinko](https://play.picoctf.org/practice/challenge/494?category=1&page=2)

# Description

History has failed us, but no matter. Server source There are two flags in this challenge. Submit flag one here, and flag two in Pachinko Revisited.

# Solution

```sh
tar -xzf server.tar.gz
```

```
POST /check HTTP/1.1
Host: activist-birds.picoctf.net:64835
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://activist-birds.picoctf.net:64835/
Content-Type: application/json
Content-Length: 48
Origin: http://activist-birds.picoctf.net:64835
Connection: keep-alive
Priority: u=0

{"circuit":[{"input1":6,"input2":8,"output":2}]}
```

Add the payload for input 1-2, output in Intruder and attack in sniper mode. and see response you will get the flag.
