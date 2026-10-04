#reverse array without changing original array
n = int(input("Enter elements in array:"))
arr= []

for i in range(n):
    arr.append(int(input("Enter array")))
    for j in arr:
        arr=arr[::-1]
print(arr)