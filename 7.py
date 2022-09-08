arr=[3,1,5,6,7,8]
n=len(arr)
for i in range(int(n/2)):
    n-=1
    temp=arr[i]
    arr[i]=arr[n]
    arr[n]=temp
print(arr)
