# Description
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

```sh
echo 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo | openssl s_client -connect localhost:30001 -ign_eof
```

[Next Level](level_16.md)
