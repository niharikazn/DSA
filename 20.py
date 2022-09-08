a=[('E',88),('s',90),('m',97),('ss',82)]
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if(a[i][1]>a[i+1][1]):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
print(a)
a="green-red-yellow-black-white"
a=a.split('-')
a.sort()
print('-'.join(a))