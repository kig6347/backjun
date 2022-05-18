hour,min = map(int,input().split())
if min - 45 < 0:
    hour = hour - 1 if hour >0 else 23
    min = 15 +min
    if min > 59: #이 조건은 필요가 없었네.
        min -= 60
else:
    min -= 45
print( hour,min)


## 다른 사람 풀이의 경우 나의 코드보다 비교 연산의 수도 가감연산의 수도 적다.
## 즉 아래가 효율성이 더 좋다는소리.
'''다른 사람
hour, min = map(int,input().split())

if min >= 45:
    print(hour, min-45)
elif hour>0 and min < 45:
    print(hour-1, min+15)
else:
    print(23, min+15)
    '''