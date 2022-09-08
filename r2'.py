n=int(input())
a=input()
b=[]
a=a.split(' ')
for i in range(n):
    a[i]=int(a[i])
for i in range(1,n+1):
        b.append(0)
for i in range(n):
    if a[i] not in b:
        b[i]=a[i]
for i in range(1,n+1):
    if i not in b:
        for j in range(n):
            if(b[j]==0):
                b[j]=i
                break
print(b)




