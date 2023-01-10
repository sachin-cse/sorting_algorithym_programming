#  take number of elements
n = int(input("Enter the number of elements:"))

# decelare arr
a = []

for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    small = i
    for j in range(i+1, len(a)):
        if a[small]>a[j]:
            small=j
    a[i],a[small] = a[small],a[i]

print("Sorted array:")
for i in a:
    print(i, end="\n")

# time complexity
# Best Case:O(n^2)
# Worst Case:O(n^2)
# Average Case:O(n^2)