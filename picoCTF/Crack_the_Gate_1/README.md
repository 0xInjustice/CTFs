[WebExpoitation](https://play.picoctf.org/practice/challenge/520?category=1&page=1)

# Description

We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: ctf-player@picoctf.org. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?

# Solution

Inspect the page and you will see comment. Use ROT13 substitution and you will see the header to include while posting data. violla youll have your flag.
