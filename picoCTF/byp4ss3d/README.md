[byp4ss3d](https://play.picoctf.org/practice/challenge/518?category=1&page=2)

# Description

A university's online registration portal asks students to upload their ID cards for verification. The developer put some filters in place to ensure only image files are uploaded but are they enough? Take a look at how the upload is implemented. Maybe there's a way to slip past the checks and interact with the server in ways you shouldn't.

# Solution

**Hint 1**
Apache can be tricked into executing non-PHP files as PHP with a .htaccess file.

upload .htaccess file and the shell.jpg
