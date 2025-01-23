'''
n = int(input("Enter the value"))
rem = 0
rev = 0
while n > 0:
    rem = n%10
    rev = rev * 10 + rem
    n //= 10
print("Reverse is:",rev)
'''

n = int(input("Enter the value"))
temp = n
fact = 1
while n > 0:
    fact *= n
    n -= 1
    print("n is",n)
print(f"Factorial of {temp} is {fact}")
