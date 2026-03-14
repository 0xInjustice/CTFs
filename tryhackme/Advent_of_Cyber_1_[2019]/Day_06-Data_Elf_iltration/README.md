# Data Elf-iltration

1. What data was exfiltrated via DNS?
   Ans: `Candy Cane Serial Number 8491`
   Name: 43616e64792043616e652053657269616c204e756d6265722038343931.holidaythief.com
   decode the hex value.

2. What did Little Timmy want to be for Christmas?
   Ans: `Pentester`
   1. Export the object by (File > Export Objects > HTTP):
   2. unzip: since we need password. We need to crack it using john.
   - `$ ./zip2john christmaslists.zip > christmaslists.hash`
   - `$ ./john christmaslists.hash `
   - Password is `december`
   3. Open the files and you'll have the answer.

3. What was hidden within the file?
   Ans: `RFC527`
   1. `teghide extract -sf TryHackMe.jpg`
   2. Use empty passphrase
