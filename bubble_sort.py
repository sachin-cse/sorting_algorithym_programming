# number of elements in the array
n = int(input("Enter number of elements : "))
  
# Below line read inputs from user using map() function 
a = []

# append element in the array
for i in range(n):
    a.append(int(input()))

# swap the element 
for i in range(0,len(a)): #time complexity this loop o(n)
    for j in range(i+1, len(a)): #time complecity this loop o(n)
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]

# sorted array
print("Sorted array:")
for i in a:
    print(i,end="\n")

# time complexity:
# Best Case: O(n)
# worst Case: O(n^2)
# average Case: O(n^2)

