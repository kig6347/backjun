a = [1,1,2,2,2,8]
b = list(map(int,input().split()))
for i in range(len(b)):
    print(a[i]-b[i],end= ' ')
