l=[14,3,6,4,58,7]
print(max(l),l.index(max(l)))
l.pop(l.index(max(l)))
print(max(l),l.index(max(l)))

l=[14,3,6,4,58,7,58]
l1=0
l2=1
if(l[l1]<l[l2]):
    l1=1
    l2=0
f=l[l1]
s=l[l2]
for i in range(2,len(l)):
    if f<l[i]:
        s=f
        f=l[i]
        l2=l1
        l1=i
    elif s<l[i] and l[i]!=f:
        s=l[i]
        l2=i
print(s,l2 ,f,l1)