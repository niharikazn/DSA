l=[14,3,6,4,58,7]
ma=l[0]
loc=0
for i in range(1,len(l)):
    if(l[i]>ma):
        ma=l[i]
        loc=i
print(loc,ma)