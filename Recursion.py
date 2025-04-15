def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print("Factorial is:",factorial(5))



def power(x,n):
    if n == 0:
        return 1
    return x * power(x,n-1)

print("Power value",power(3,2))
'''
sum of digit=235
2+3+5 = 10'''
'''
do reverse a number n = 123
rev = 321'''
