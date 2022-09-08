def bi(arr,e,l,h):
    mid=int((l+h)/2)
    if(arr[mid]==e):
        print("found",mid)
    elif(arr[mid]>e):
        bi(arr,e,0,mid)
    else:
        bi(arr,e,mid+1,h)
arr=[1,2,3,4,5,6,7,8,9]
bi(arr,8,0,8)
