# math 함수 사용 문제
a,b,v = map(int,input().split())
day = 1
if a > v:
    print('1')
else:
    v -= a
    print((v // (a-b)) + 2 if (v / (a-b))> (v // (a-b)) else (v // (a-b)) + 1)

'''# 다른사람
## 올림 문제여서 올림 사용함
import math

a, b, v = map(int, input().split())
# a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

day = math.ceil((v-a)/(a-b)) + 1
print(day)
'''