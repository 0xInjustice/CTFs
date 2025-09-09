# decription
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    human-readable
    1033 bytes in size
    not executable

```bash
find . -size 1033c
```

 M, G and c for Mb, Gb and byte specific respectively
 +2G for more than 2Gb
 -2G for less than 2Gb

**List and File Size Display**
 ```bash
 find /etc -size +5M -exec ls -sh {} +
 ```
**exec** for executing commands
