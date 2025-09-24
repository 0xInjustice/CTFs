[Scavenger Hunt](https://play.picoctf.org/practice/challenge/161?category=1&page=2)

# Description
There is some interesting information hidden around this site `http://mercury.picoctf.net:44070/.` Can you find it?

# Solution

1. View the page source you'll get the first part of the flag `picoCTF{t`
2. Go to the mycss.css file you'll get second part of the flag `h4ts_4_l0`
3. In myjs.js you'll get a hint `How can I keep Google from indexing my website? `. which is `robots.txt`. By accessing it you'll get third flag `t_0f_pl4c`. You'll also get the fouth hint there `I think this is an apache server... can you Access the next flag?`
4. By accessing the .htaccess file you'll get flag `3s_2_lO0k` and hint `I love making websites on my Mac, I can Store a lot of information there.`
5. Go to .DS_Store and youll have the flag `_7a46d25d}`

```markdown
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k__7a46d25d}
```

