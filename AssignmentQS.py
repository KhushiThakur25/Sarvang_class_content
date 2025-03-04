Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fact(n):
...     f = 1
...     for i in range(n+1):
...         f *= i
...     return f
... 
>>> fact(5)
0
>>> def fact(n):
...     f = 1
...     for i in range(2,n+1):
...         f *= i
...     return f
... 
>>> fact(5)
120
>>> 5*4*3*2*1
120
li = [1,2,5,1,4,6,7,8,2]

set(li)
{1, 2, 4, 5, 6, 7, 8}
li
[1, 2, 5, 1, 4, 6, 7, 8, 2]
unique_list = []
def remove_duplicate(li):
    for item in li:
        if item not in unique_list:
            unique_list.append(item)

remove_duplicate(li)
unique_list
[1, 2, 5, 4, 6, 7, 8]
def pascal(5):
    
SyntaxError: invalid syntax
def pascal(n):
    for i in range(n):
        value = 1
        for j in range(i+1):
            print(value,end = " ")
            value  = value * (i-j) // (j + 1)
        print()

pascal(5)
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
def pascal(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end = " ")
        value = 1
        for j in range(i+1):
            print(value,end = " ")
            value  = value * (i-j) // (j + 1)
        print()

pascal(5)
        1 
      1 1 
    1 2 1 
  1 3 3 1 
1 4 6 4 1 
def pascal(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end = " ")
        value = 1
        for j in range(i+1):
            print(value,end = "  ")
            value  = value * (i-j) // (j + 1)
        print()
pascal(5)
SyntaxError: invalid syntax
def pascal(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end = " ")
        value = 1
        for j in range(i+1):
            print(value,end = "  ")
            value  = value * (i-j) // (j + 1)
        print()

pascal(5)
        1  
      1  1  
    1  2  1  
  1  3  3  1  
1  4  6  4  1  
def pascal(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end = "")
        value = 1
        for j in range(i+1):
            print(value,end = "  ")
            value  = value * (i-j) // (j + 1)
        print()

pascal(5)
    1  
   1  1  
  1  2  1  
 1  3  3  1  
1  4  6  4  1  
def pascal(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end = "")
        value = 1
        for j in range(i+1):
            print(value,end = " ")
            value  = value * (i-j) // (j + 1)
        print()

pascal(5)
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
for i in range(5):
    print(11 * i,end = " ")

0 11 22 33 44 
for i in range(5):
    print(11 ** i)

1
11
121
1331
14641
for i in range(6):
    print(11 ** i)

1
11
121
1331
14641
161051
pascal(6)
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 
