Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='mothers'
t=s.capitalize()
print(t)
Mothers
t=s.title()
print(t)
Mothers
s='mothers public school'
t=s.upper()
print(t)
MOTHERS PUBLIC SCHOOL
s='abc@123'
p='123'
s.isdigit()
False
p.isdigit()
True
s='mothers public school'
s.startwith('m')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.startwith('m')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startswith('m')
True
s.startswith('mo')
True
]
s.startswith('Mo')
False
s[:7].endswith(s)
False
print(s)
mothers public school
s[:7].endswith(s)
False
s[:7].endswith('s')
True
s='god is good'
s.isupper()
False
s[2].isupper()
False
s.index(0)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.index(0)
TypeError: must be str, not int
s.index('0')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.index('0')
ValueError: substring not found
s.index('o')
1
s.count('o')
3
s.split()
['god', 'is', 'good']
t='john is a naughty boy'
t.split(' ',2)
['john', 'is', 'a naughty boy']
