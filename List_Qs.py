'''
x = [3,2,1,5,6,8,7,4,10]

min_ = x[0]
max_ = x[0]
sum_ = 0
sum_li = 0
for i in x:
    if min_ > i:
        min_ = i
for i in x:
    if max_ < i:
        max_ = i

for i in range(min_,max_+1,1):
    sum_ += i
for i in x:
    sum_li += i

missing_value = sum_ - sum_li
print("Your missing value is: ",missing_value)
'''
x=[0,0,2,2,1,2,0,1,2,0,1,1]
a=0
b=0
c=0
for i in x:
    if i == 0:
        a=a+1
for i in x:
    if i == 1:
        b=b+1
for i in x:
    if i == 2:
        c=c+1
print(f"a is {a} and b is {b} and c is {c}")
for i in range(len(x)):
    if i < a:
        x[i] = 0
    elif i >= a and i < a+b:
        x[i] = 1
    else:
        x[i] = 2
print(x)











