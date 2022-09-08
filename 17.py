arr=[-1,-1,6,1,9,3,2,-1,4,-1]
for i in range(len(arr)):
    if(arr[i]!=-1):
        temp=arr[arr[i]]
        arr[arr[i]]=arr[i]
        arr[i]=temp
print(arr)