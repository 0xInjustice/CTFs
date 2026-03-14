# Training

1.  How many visible files are there in the home directory(excluding ./ and ../)?
    Ans:8

2.  What is the content of file5?
    Ans:recipes

3.  Which file contains the string ‘password’?
    Ans:file6
    `   grep -r "password" .
./file6:passwordHpKRQfdxzZocwg5O0RsiyLSVQon72CjFmsV4ZLGjxI8tXYo1NhLsEply`

4.  What is the IP address in a file in the home folder?
    Ans: `10.0.0.05`
    use the command `egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" *`

5.  How many users can log into the machine?
    Ans: 3, 2 + root

6.  What is the sha1 hash of file8?
    Ans:`fa67ee594358d83becdd2cb6c466b25320fd2835`
    `[mcsysadmin@ip-10-49-188-126 ~]$ sha1sum file8
fa67ee594358d83becdd2cb6c466b25320fd2835  file8`

7.  What is mcsysadmin’s password hash?
    Ans:`$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/`
    1. find / -name shadow\* 2>/dev/null | head
       /var/shadow.bak
       cat /var/shadow.bak
