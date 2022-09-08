def lr(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
arr=[1,3,2,4,5]
i=1
while(i):
    lr(arr,5)
    i-=1
print(arr)