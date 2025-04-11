li = [1,3,5,6,7,9]
target = 17
left = 0
right = len(li)-1

while left < right:
    mid = (left + right)//2
    if li[mid] == target:
        print("Element found")
    elif li[mid] < target:
        left = mid + 1
    elif li[mid] > target:
        right = mid - 1
    else:
        print("Element not found")li = [1,3,5,6,7,9]
target = 1
left = 0
right = len(li)-1

result = False
while left <= right:
    mid = (left + right)//2
    if li[mid] == target:
        result = True
        break
    elif li[mid] < target:
        left = mid + 1
    elif li[mid] > target:
        right = mid - 1
    
if result:
    print("Element Found")
else:
    print("Element not found")
