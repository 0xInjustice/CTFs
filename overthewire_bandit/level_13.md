# Decription
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

# Solution
```sh
ssh -i <private_key> bandit14@localhost -p 2220
cd /etc/bandit_pass/
cat bandit14
```

[Next Level](level_14.md)
