[**Unrestricted File Upload**](https://play.picoctf.org/practice/challenge/482)

# Description
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.

Whenever you get a shell on a remote machine, check ``sudo -l``
upload the script `shell.php`
then go and execute command `https://website/uploads/shell.php?cmd=ls`
