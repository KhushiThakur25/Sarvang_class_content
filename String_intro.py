Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "hello"
>>> type(st)
<class 'str'>
>>> st[1]
'e'
>>> st[0]
'h'
>>> st[2]
'l'
>>> st[4]
'o'
>>> st[5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    st[5]
IndexError: string index out of range
>>> st[0] = 'm'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    st[0] = 'm'
TypeError: 'str' object does not support item assignment
a = 0
a
0
a = 5
a
5
del st[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del st[0]
TypeError: 'str' object doesn't support item deletion
del st
st = "This Is PYTHon Language"
st.upper()
'THIS IS PYTHON LANGUAGE'
st
'This Is PYTHon Language'
st = st.upper()
st
'THIS IS PYTHON LANGUAGE'
st = "This Is PYTHon Language"
st.lower()
'this is python language'
st.title()
'This Is Python Language'
st.swapcase()
'tHIS iS pythON lANGUAGE'
st.isalpha()
False
a = "hello"
a.isalpha()
True
b = '12345'
b.isnumeric()
True
b.isdigit()
True
c = 'jbdf1234'
c.isnumeric()
False
c.isdigit()
False
c.isaplnum()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.isaplnum()
AttributeError: 'str' object has no attribute 'isaplnum'. Did you mean: 'isalnum'?
c.isalnum()
True
st
'This Is PYTHon Language'
st.replace('s','q')
'Thiq Iq PYTHon Language'
st.replace('s','q',1)
'Thiq Is PYTHon Language'
st.index('i')
2
st.index('is')
2
st.index('z')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    st.index('z')
ValueError: substring not found
st.find('i')
2
st.find('z')
-1
