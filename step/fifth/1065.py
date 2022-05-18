#     a = i//100
#     b = (i//10)%10
#     c = i%10
# 이방식보다 --> 연산또는 '=' 대입연산자에서 시간 차이가 있는듯 --> 76ms
# list() 를 사용하면 연산을 아낄수 있다. --> 68ms
## but 메모리 차이는 없지만 시간이 차이가 난다.


import sys
su = int(sys.stdin.readline())
count = 0
if su < 100:
    count = su
else:
    count = 99

for i in range(100,su+1):## su+1 이 중요
    '''
    a = i//100
    b = (i//10)%10
    c = i%10
    #if a[0]-a[1] == a[1]-a[2]:
    if a-b == b-c:
    ''' # 위의 방식으로 했을때 76ms
    a = list(map(int,str(i))) # 이 방식으로 했을떄 68ms 
    ## but 메모리 사용량은 동일, 하지만 '= ' 에 소비되는 시간이 걸리거나 연산 시간일듯
    if a[0]-a[1] == a[1]-a[2]:
        count += 1
print(count)

