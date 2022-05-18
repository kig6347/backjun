# 숫자로 풀기, 문자로 풀기
# 브루트 포스일듯
#나눗셈에서는 항상 zerodivision 조심!!
# 다른 풀이는 그냥 곱한다 같긴한데
#내가 연산이 더 적어


a = []
[a.append(int(i)) for i in input()]

b=1
c=1
if len(a) == 1:
    print('NO')
else:
    for i in range(len(a)):
        c *= a[i]
    d = 1
    for i in a:
        b *= i
        if i != 0:
            c //= i
        else:
            c = 0
        if b == c:
            print('YES')

            break
        # if b == d and c == 1:## 1221때문에 안돼. 물론 break 쓰면 되지만 끝까지 비교를 안하게 되서 안돼
        d += 1
        if d == len(a):  # 조건을 하느니 count를 셌어
            print('NO')
            break
        # elif i == a[len(a)-1]: # 인덱스가 아닌 value로 비교해서 안돼 반례:4729382 넣어보셍 2가 2개면서 마지막이라 두번뜰꺼임