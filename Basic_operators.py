'''
Arithemtic operators:
    1. Addition -> 3+4 => 7
    2. Subtract -> 5-2 => 3
    3. multiplication -> 2*3 => 6
    4. division(float division) -> 5/2 => 2.5
    5. floor division -> 5//2 => 2
    6. modulus -> 5%2 => 1
    7. exponent -> 2 ** 2 => 4
'''

a = 23
b = 45
x = 3
y = 51

print(a+x*b)
#158
print(x + y *2)
#105
print(a // b , a % b)
#0 , 23
print(x + y * 3 - (x // a))
#156

'''
Comparison operator

  1.equals to -> ==
  2.not equals to -> !=
  3.greater than -> >
  4.lesser than -> <
  5.greater than equals to -> >=
  6.lesser than equals to -> <=
'''
a = 2
b = 2
c = 5
print(a == b)
print(a != b)
print(a > c)
print(a <= b)
print(b >= c)
print(b < c)


a = 15
b = 3
c = a+b
d = 56
e = 89
f = 23
# values of a=_ ,b=_,c=_,d=_,e=_,and f=_.

print("What is the sum of a and b..?")
print(a+b)


print("do sum of a+b with 2",c+2,sep = "->")

print(f"values of a={a} ,b={b},c={c},d={d},e={e},and f={f}.")
