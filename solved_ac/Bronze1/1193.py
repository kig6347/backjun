import time
x = int(input())
n = 1
line = 1
start_time = time.time()
'''
while True:
    if ((n ** 2) + n) // 2 >= x:
        n -= 1
        x -= ((n ** 2) + n) // 2
        n += 2
        break
    n += 1

if (n+1) % 2: # 홀수
    qnswk = n-x
    qnsah = x
else:
    qnswk = x
    qnsah = n-x
print('{0}/{1}'.format(qnswk,qnsah))
''' #주석이 내 방식인데 time =  0.0009975433349609375, 후자가 time =  0.0 로 압도적이네.
#곱하기 보다 덧셈 뺄셈이 더 빠르데
while x >line :
    x -= line
    line += 1
if line % 2 == 0:
    a= x
    b = line -x +1
else:
    a= line -x +1
    b =x
print(a,"/",b,sep='')
print('time = ',time.time()-start_time)


