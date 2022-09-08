def mh(arr,n,k):
    mod=k%n
    s=" "
    for i in range(n):
        print(str(arr[(mod+i)%n]))
arr=[2,4,6,8,4,3,1]
mh(arr,7,3)