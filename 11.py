a = int(input())
j = 1
while (a):
    l = []
    l.clear()
    d = 0
    e = 0
    b = int(input())
    for i in range(0, 2 * b):
        c = input()
        l.append(c)
    for i in range(0, b):
        d += l[i].count('I')
    for i in range(b , 2 * b):
        e += l[i].count('I')
    a-=1
    print('Case #'+str(j)+": "+str(abs(d - e)))
    j+=1




