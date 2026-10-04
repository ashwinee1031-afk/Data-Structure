#accept N integers into array and calculate sum of all elements. 


n = int(input("Enter number of elements (N)"))
arr = []

print(f"Enter {n} integers:")
for i in range (n):
    element = int(input(f"Element {i+1}:"))
    arr.append(element)
    
array_sum = sum(arr)
print(f"The sum of all elements in the array is :{array_sum}")    