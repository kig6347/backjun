## a = [1,2,3,4,5,6,7,8,9,10] ---> a[:0] = [] , a[:1] =[1]
import time
a=  int(input())
for _ in range(a):
    k = int(input()) # 0~
    n = int(input()) # 1~
    a_time = time.time()
    a = [[i for i in range(1,n+1)]]
    for i in range(k):# 0부터이긴한데 위에서 만들어줘서 괜찮음 ,어차피 순서만 지키는거라서
        a.append([sum(a[i][:j]) for j in range(1,n+1)])
    print('a_time=',time.time())
    b_time = time.time()
    f0 = [x for x in range(1, n+1)]  # 0층 리스트
    for k in range(k):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print('b_time=',time.time())
    print(a[-1][-1])


'''# 다른사람
### 내코드 84ms. 다른 사람코드 80ms
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력

'''









# q qqqqqw qqqqqqqqqqqqqqwwwwwe qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwweeeeer
# q qqqqw qqqqqqqqqwwwwe qqqqqqqqqqqqqqqqqqqwwwwwwwwwweeeer
# q qqqw qqqqqqwwwe qqqqqqqqqqwwwwwweeer
# q qqw qqqwwe qqqqwwweer
# q qw qwe qwer qwert
# q w e r t