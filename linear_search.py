def linear_search(arr, n, value):
    for i in range(0,n):
        if arr[i] == value:
            return i
    return -1

a = []
num = int(input())
for i in range(num):
    a.append(int(input("Enter the input:")))

key = int(input("Enter the finding value:"))
res = linear_search(a, num, key)

if res == -1:
    print("Element not found")
else:
    print(f"Element found at {i} position")

# time complexity
# Best Case:O(1)
# Worst Case:O(n)
# Average Case:O(n)



