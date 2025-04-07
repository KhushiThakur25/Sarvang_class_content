'''n = int(input("Enter the number.."))
org = n
count = 0
sum_ = 0
while n > 0:
    count += 1
    n //= 10
print("count is: ",count)
n = org
print("n is",n)

while n > 0:
    rem = n%10
    sum_ += pow(rem,count)
    n //= 10
print("sum is",sum_)
n = org
if sum_ == n:
    print("Number is an Armstrong..")
else:
    print("Number is not an Armstrong")
    '''
n = 4
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end = " ")
    print()
