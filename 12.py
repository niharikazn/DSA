arr=[1,2,55,22,33,5,7,8]
s=40
for i in range(0,8):
    for j in range(i,8):
        if(s==(arr[i]+arr[j])):
            print(arr[i], arr[j])