# File Confusion

1. How many files did you extract(excluding all the .zip files)
   Ans:50

2. How many files contain Version: 1.1 in their metadata?
   Ans:3
   1. `for file in *; do exiftool "$file" | grep "1.1"; done`

3. Which file contains the password?
   Ans:`grep -nr  "password" .
./dL6w.txt:27:password is 'scriptingpass'`
