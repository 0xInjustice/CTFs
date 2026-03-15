# Elfcryption

1. What is the md5 hashsum of the encrypted note1 file?
   Ans:`md5sum note1.txt.gpg
24cf615e2a4f42718f2ff36b35614f8f  note1.txt.gpg `

2. Where was elf Bob told to meet Alice?
   Ans:
   1. Get the hint
   2. use gpg to Decrypt `gpg -d note1.txt.gpg`

3. Decrypt note2 and obtain the flag!
   Ans:`THM{ed9ccb6802c5d0f905ea747a310bba23} `
   1. Get the hint.
   2. Run openssl to decrypt `openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out plaintext.txt`
