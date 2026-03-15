# Accumulate

1. A web server is running on the target. What is the hidden directory which the website lives on?
   Ans:` /retro`
   1. Run gobuster `gobuster dir -url http://10.48.181.72/ -w ~/hack/wordlists/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt -t 200`

2. Gain initial access and read the contents of user.txt
   Ans:
   1. Look in the retro folder and click all and go to recent comment. You'll see `Parzival`
   2. Use it as password for account `wade`.
   3. He might use same credentials for remote-desktop. Which we can access using `remmina`
   4. cat the user.txt `THM{HACK_PLAYER_ONE}`

3. [Optional] Elevate privileges and read the content of root.txt
   Ans: THM{COIN_OPERATED_EXPLOITATION}
