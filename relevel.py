t=int(input())
while t:
    n=int(input())
    flag=0
    for i in range(int(n/2)):
        c=i*i*i*i
        for j in range(1,int(n/2)):
            d=c+(j*j*j*j)
            if(d==n):
                flag=1
    if(flag==1):
        print(1)
    else:
        print(0)

