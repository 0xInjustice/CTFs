# Evil Elf

1. Whats the destination IP on packet number 998?
   Ans:63.32.89.195
   1. Open the pcap file and get your answer

2. What item is on the Christmas list?
   Ans: ps4
   1. Filter out the destination ip. You can see the TELENT commands.

3. Crack buddy's password!
   Ans: `rainbow`
   1. `ip.dst == 10.10.186.136 and tcp.port==39390` since /etc/shadow's value is sent from dest to src this filter should be userd.
   2. Data: buddy:$6$3GvJsNPG$ZrSFprHS13divBhlaKg1rYrYLJ7m1xsYRKxlLh0A1sUc/6SUd7UvekBOtSnSyBwk3vCDqBhrgxQpkdsNN6aYP1:18233:0:99999:7:::\n
   3. Crack the hash:
   - Find what kind of has is it: SHA512
   - use john: `john hash --show`
