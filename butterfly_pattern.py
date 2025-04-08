'''n = 4
for i in range(1,n+1):
    print("*"*i + " "*(2*(n-i))+"*"*i)
for i in range(n-1,0,-1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
'''

'''
word1 = "listen"
word2 = "silent"

str1 = word1.replace(" ","").lower()
str2 = word2.replace(" ","").lower()

x = sorted(str1)
y = sorted(str2)
if x == y:
    print("String is an anagram")
else:
    print("String is not an anagram")
'''
'''
st = input("Enter the string").lower()
count = 0
for i in st:
    if i in ["a","i","o","u"]:
        print(i)
        count += 1
print("Count of vowels is",count)
'''
'''
st = input("Enter the string").lower()
count = 0
for i in st:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)
        count += 1
print("Count of vowels is",count)
'''
li = [3,4,5,6,1,2,5,4]
'''
for i in range(0,len(li),1):
    leader = True
    for j in range(i+1,len(li),1):
        if li[i] < li[j]:
            leader = False
            break
    if leader:
        print(li[i])

'''











