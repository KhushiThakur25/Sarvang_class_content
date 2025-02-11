Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = list()
>>> li
[]
>>> li.append(23)
>>> li
[23]
>>> li.append('notebook')
>>> li
[23, 'notebook']
>>> li.append('pencil','bottle','bag')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    li.append('pencil','bottle','bag')
TypeError: list.append() takes exactly one argument (3 given)
>>> li.append(['pencil','bottle','bag'])
>>> li
[23, 'notebook', ['pencil', 'bottle', 'bag']]
>>> li.extend(['pencil','bottle','bag'])
li
[23, 'notebook', ['pencil', 'bottle', 'bag'], 'pencil', 'bottle', 'bag']
li.remove(['pencil', 'bottle', 'bag'])
li
[23, 'notebook', 'pencil', 'bottle', 'bag']
li.index('pencil')
2
li[2] = 'pen'
li
[23, 'notebook', 'pen', 'bottle', 'bag']
li.insert(2,'book')
li
[23, 'notebook', 'book', 'pen', 'bottle', 'bag']
len(li)
6
li.pop()
'bag'
li
[23, 'notebook', 'book', 'pen', 'bottle']
li = [1,2,3,2,12,12,13,1,5,5,6,7]
li.count(12)
2
li.reverse()
li
[7, 6, 5, 5, 1, 13, 12, 12, 2, 3, 2, 1]
li.sort()
li
[1, 1, 2, 2, 3, 5, 5, 6, 7, 12, 12, 13]
li.sort(reverse = True)
li
[13, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
max(li)
13
min(li)
1
sum(li)
69
k = [23,56,74,85,96]
k.clear()
k
[]
k = [23,56,74,85,96]
del k
k
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    k
NameError: name 'k' is not defined
li
[13, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
m = li
m
[13, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
m[0]
13
m[0]=  100
m
[100, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
li
[100, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
m = li.copy()
m
[100, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
li
[100, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
m[0] = 200
m
[200, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
li
[100, 12, 12, 7, 6, 5, 5, 3, 2, 2, 1, 1]
