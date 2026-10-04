#program to accept N integers into an array and display largest element , second largest element,
#smallest element and second smallest element.

arr=[10,5,6,743,23,45,6]
max=min=arr[0]
smax=smin=arr[0]
for num in arr:
    if num > max:
        smax=max
        max=num
    elif(num>smax and num!=max):
        smax=num
    if num < min :
        smin=min
        min=num
    elif(num<smin and num!=min):
        smin=num
print("Maximum",max)
print("Minimum",min)
print("Second max",smax)
print("Second min",smin)                   
