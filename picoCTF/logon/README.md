[logon](https://play.picoctf.org/practice/challenge/46?category=1&page=2)

# Description
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/15796/ 

# Solution

Keep the intercept on and login. When it sends the data backto browser change `Admin=False` to `True`. Violla!!!! you'll have the flag.
