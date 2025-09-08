[PIE TIME](https://play.picoctf.org/practice/challenge/490)

# Description
Can you try to get the flag? Beware we have PIE!

# process
1. analyze [vuln.c](vuln.c)
2. if you manage to find the address of the win function then you can execute it to find the flag
3. use `nm`. GNU nm lists the symbols from object files objfile
```bash
nm vuln
```
4. compare the address of main in CTF and local objfile.
5. find the flag and submit

