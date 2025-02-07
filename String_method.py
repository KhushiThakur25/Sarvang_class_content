Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "This is python language"
>>> st.split()
['This', 'is', 'python', 'language']
>>> st
'This is python language'
>>> s = st.split()
>>> s
['This', 'is', 'python', 'language']
>>> type(s)
<class 'list'>
>>> " ".join(s)
'This is python language'
>>> "-".join(s)
'This-is-python-language'
>>> " + ".join(s)
'This + is + python + language'
>>> st = "    this is python    "
>>> st.lstrip()
'this is python    '
st.rstrip()
'    this is python'
st.strip()
'this is python'
st = 'hello'
st[-2]
'l'
st[-1]
'o'
st[0]
'h'
st[1:4:1]
'ell'
st[::-1]
'olleh'
st = input("Enter the string..")
Enter the string..this is the python
st
'this is the python'
st = st.split()
st
['this', 'is', 'the', 'python']
for i in range(len(st)):
    if len(st[i])%2 == 0:
        print(st[i])

this
is
python
for i in st:
    print(i)

this
is
the
python
for i in st:
    if len(i)%2 == 0:
        print(i)

this
is
python
