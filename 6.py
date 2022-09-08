def lr(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

arr=[1,3,2,4,5]
i=2
while(i):
    lr(arr,5)
    i-=1
print(arr)