# Skilling Up

1. how many TCP ports under 1000 are open?
   Ans: 3
   1. use Nmap:
      ```scan
      injustice@omega:~-$ nmap -p 1-1000 10.48.141.18
      Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-15 10:19 +0530
      Nmap scan report for 10.48.141.18
      Host is up (0.086s latency).
      Not shown: 997 closed tcp ports (conn-refused)
      PORT STATE SERVICE
      22/tcp open ssh
      111/tcp open rpcbind
      999/tcp open garcon
      ```

2. What is the name of the OS of the host?
   Ans: Linux

   ```output
   No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
   TCP/IP fingerprint:
   OS:SCAN(V=7.98%E=4%D=3/15%OT=22%CT=7%CU=34224%PV=Y%DS=3%DC=I%G=Y%TM=69B63E4
   OS:7%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)SEQ
   OS:(SP=104%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=104%GCD=1%ISR=10C%TI=Z%
   OS:CI=Z%II=I%TS=A)SEQ(SP=104%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=106%G
   OS:CD=1%ISR=104%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M4E8ST11NW6%O2=M4E8ST11NW6%O3=M4
   OS:E8NNT11NW6%O4=M4E8ST11NW6%O5=M4E8ST11NW6%O6=M4E8ST11)WIN(W1=68DF%W2=68DF
   OS:%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=FF%W=6903%O=M4E8NNSNW6%C
   OS:C=Y%Q=)T1(R=Y%DF=Y%T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%
   OS:T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%RD
   OS:=0%Q=)T6(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=FF%W=0%S
   OS:=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%UN=0%RIPL=G%RID=G%RIPCK
   OS:=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=FF%CD=S)

   ```

3. What version of SSH is running?
   Ans: 7.4

4. What is the name of the file that is accessible on the server you found running?
   Ans:`interesting.file`
5. visit the <ip>:999 you will get a file.
