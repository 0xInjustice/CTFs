# Description
The password for the next level is stored somewhere on the server and has all of the following properties:
    owned by user bandit7
    owned by group bandit6
    33 bytes in size

```bash
find . -size 33c -exec ls -l {} + | grep bandit6 
6     33 Aug 15 13:16 ./var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
```

[Next Level](level_07.md)
