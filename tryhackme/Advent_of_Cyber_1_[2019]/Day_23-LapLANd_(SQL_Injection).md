# LapLANd (SQL Injection)

[doc](https://docs.google.com/document/d/15XH_T1o6FLvnV19_JnXdlG2A8lj2QtepXMtVQ32QXk0/edit?tab=t.0)

use sqlmap

1. Which field is SQL injectable? Use the input name used in the HTML code.
   Ans:`log_email`

2. What is Santa Claus' email address?
   Ans:`bigman@shefesh.com`

3. What is Santa Claus' plaintext password?
   Ans:`saltnpepper`

4. Santa has a secret! Which station is he meeting Mrs Mistletoe in?
   Ans:`Waterloo station`

5. Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/
   Ans:`THM{SHELLS_IN_MY_EGGNOG} `
   1. upload a php reverse shell
   2. use phtml extension instead of php since its blocked.
