#count even and odd elements in the array 

n = int(input("Enter number of elements in array"))

print(f"Enter {n} integers")
arr = [int(input())for _ in range(n)]

even_count=0
odd_count=0

for num in arr:
    if num %2==0:
        even_count+=1
    else:
        odd_count+=1

print(f"Number of Even elements:{even_count}")
print(f"Number of odd elements:{odd_count}")
    
        