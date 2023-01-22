def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low<=high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid
    return -1

arr = []
n = int(input("Enter the number of element present in the array:"))
print("Enter the element in the array:")
for i in range(n+1):
    arr.append(int(input()))
print("Enter the value which you find:")
x = int(input())


res = binary_search(arr,x)
if res==-1:
    print(f'{x} is not present in the array:')
else:
    print(f'{x} is present in the array:')

# time complexity
# O(logn)

