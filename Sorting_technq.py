li = [64,34,25,12,22,11]
#bubble sort
'''
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]

print(li)
'''
#selection sort
for i in range(len(li)):
    min_index = i
    for j in range(i+1,len(li)):
        if li[j] < li[min_index]:
            min_index = j
    li[i],li[min_index] = li[min_index],li[i]

print(li)
