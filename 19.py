a=int(input())
n=2*a
c=a+1
print("*"*(a+1),end='')
while(n!=1):
    print("*",end='')
    n=int(n/2)
    c+=1
print("")
print(" "+"*"+" "*(c-4)+"*")
c=2
while(a):
    print(" "*(c)+"*"*a)
    c+=1
    a=int(a/2)




