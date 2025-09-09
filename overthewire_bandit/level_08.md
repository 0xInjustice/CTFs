# Description
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

```bash
sort data.txt | uniq -u
# or
awk '{arr[$0]++};END{for(var in arr) if (arr[var] == 1) print var}' data.txt
```

[Next Level](level_09.md)
