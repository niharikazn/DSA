def rr(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
def lr(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
arr=[15,18,2,3,6,12]
i=0
while(min(arr)!=arr[0]):
    lr(arr,6)
    i+=1
print(arr)
print(i )