a,b,c = map(int, input().split())
count = 1
if b >= c:  ## 부등호 중요해 zerodivisionError 나올수 있어
    print('-1')
else:
    print((a//(c-b))+1)
    #print(int(a / (c - b) + 1))