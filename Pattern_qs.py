Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input("Enter the number.."))
Enter the number..5
>>> for i in range(0,n,1):
...     for j in range(0,i+1,1):
...         print("*",end = " ")
...     print()
... 
* 
* * 
* * * 
* * * * 
* * * * * 
>>> n
5
>>> for i in range(0,5,1):
...     for j in range(0,5-i,1):
...         print("*",end = " ")
...     print()

* * * * * 
* * * * 
* * * 
* * 
* 
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end = " ")
    print()

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
