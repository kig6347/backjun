#import time
wkdus = list(map(int,input().split()))
start = min(wkdus)
#start_time = time.time()
while True:
    cnt = 0
    for j in wkdus:
        if start % j == 0:
            cnt += 1
    if cnt >= 3 :
        print(start)
        break
    start += 1

#print('time = {}'.format( time.time()-start_time))