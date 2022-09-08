for a in range(2,30):
    flag=0
    if(a>1):
        for i in range(2,a):
            if(a%i)==0:
                flag=1
                break
            else:
                flag=0
a=[x for x in range(30)]
n=30
def crossout(a,n,k):
    if a[k]==1:
        return
    for l in range(2*k,n,k):
        a[l]=1
    return
for k in range(2,int(pow(n,0.5))):
    crossout(a,n,k)
print(a)
