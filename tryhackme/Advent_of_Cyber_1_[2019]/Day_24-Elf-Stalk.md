# Elf Stalk

1. Find the password in the database
   Ans:`9Qs58Ol3AXkMWLxiEyUyyf`
   1. run nmap on all ports
   2. make an API request to `curl "http://10.49.151.229:9200/_search?q=password" | jq`

2. Read the contents of the /root.txt file
   Ans:`someELKfun`
