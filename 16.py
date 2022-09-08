def lr(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
arr=[2,4,6,8]
b=[2,4,6,8]
k=4
s=0
while(k):
    k-=1
    c=0
    for i in range(4):
        if(arr[i]!=b[i]):
            c+=1
            c+=1
    if(s<c):
        s=c
    lr(arr, 4)
print(s)

