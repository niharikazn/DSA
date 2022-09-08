def lr(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
arr=[10,1,2,3,4,5,6,7,8,9]
s=0
k=0
for i in range(0,10):
    l=[i*arr[i] for i in range(len(arr))]
    print(sum(l))
    if(sum(l)>s):
        s=sum(l)
        k=i
    lr(arr,10)

print(s,k)