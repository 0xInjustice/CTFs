[Reverse Engineering](https://play.picoctf.org/practice/challenge/472)
# Description
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you. The program's source code can be downloaded here.

Additional details will be available after launching your challenge instance.

# Solution
We know that the script takes user input, and this input isn’t sanitized:

```python
elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
```

We also know that we can use the RETURN command to force the reader to read any specific line:

```python
elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
```

Since we know that the verse containing our flag starts at the very beginning, we need to pass RETURN 0 to the script. However, if we do this, the script will simply echo RETURN 0 back to us, treating it as a string. To make sure the script interprets RETURN 0 as a command rather than a string, we need to adjust our input slightly.
Get Pi - The Kernel Panic’s stories in your inbox

Join Medium for free to get updates from this writer.

Instead of just using RETURN 0, we will use some_string;RETURN 0.
