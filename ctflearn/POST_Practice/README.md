[POST Practice](https://ctflearn.com/challenge/114)

# Description

This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php

# Solution

Instead of usingh GET to access the website change the rrequest to POST

```sh
curl -X POST http://165.227.106.113/post.php \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"71urlkufpsdnlkadsf"}'
```
