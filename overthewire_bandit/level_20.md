# Level Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

# A little bit of Theory
Netcat or nc was introduced in level 15. To create a server on localhost, the -l flag (which means listening) is needed. To specify a port, the -p flag is needed. To create a “onetime server”, a server that sends one message and then disconnects, we can use the pipe (| - level 6) and echo to input the message.

If a command needs to be run, but you don’t need to interact with it for a while and want to keep using the same terminal with other commands while the command is executing, you can use &. The ampersand will send the command in the background. This is a part of the Linux process management. Specifically, if you want to learn more about this, also look into the jobs command, it shows processes/commands/jobs running in the background and foreground.

# Solution

```sh
echo -n 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j' | nc -l -p 1234 &
./suconnect 1234
```

[Next Level](level_21.md)
