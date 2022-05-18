a,b = map(int,input().split())
c = list(map(int,input().split()))
d = a*b
for i in c:
    print(i - d, end = " ")
