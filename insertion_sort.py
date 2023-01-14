def insertion(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1

        while j>=0 and temp<a[j]:
            a[j+1] = a[j]
            j= j-1

        a[j+1] = temp
    
def printarr(a):
    for i in range(len(a)):
        print(a[i], end="\t")

a = []
n = int(input())
for i in range(n+1):
    a.append(int(input("Enter the input:")))

print("Before sorting:")
printarr(a)

insertion(a)
print("\n After Sorting:")
printarr(a)

# time complexity
# Best Case:O(n)
# worst Case:O(n^2)
# Average Case:O(n^2)





