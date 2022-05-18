num = int(input())
for _ in range(num):
    h,w,n = map(int,input().split())
    if not n%h:
        print(h*100+n//h)
        continue
    #print((n%h * 100) + (n // h + 1))
    print('{}{:02}'.format((n%h),(n//h)+1))

