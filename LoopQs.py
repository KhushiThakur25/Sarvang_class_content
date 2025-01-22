'''2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
n = int(input("Enter the number"))
# initialization
x = 1
# stop condition/termination condition
while x <= 10:
    print(f"{n} x {x} = {n*x}")
    #updation
    x += 1
'''

n = int(input("Enter the number"))
i = 1

sums = 0
while i <= n:
    sums = sums + i
    i += 1
print(sums)
