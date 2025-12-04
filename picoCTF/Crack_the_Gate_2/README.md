[Web Exploitation](https://play.picoctf.org/practice/challenge/521?category=1&page=2)

# Description

The login system has been upgraded with a basic rate-limiting mechanism that locks out repeated failed attempts from the same source. We’ve received a tip that the system might still trust user-controlled headers. Your objective is to bypass the rate-limiting restriction and log in using the known email address: ctf-player@picoctf.org and uncover the hidden secret.

# Solution

Add X-Forwarded-For: 1.2.3.4 to header and the perform a pitchfork attack with password.txt
