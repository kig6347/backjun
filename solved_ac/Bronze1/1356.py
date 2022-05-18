#꼭 다시 하셈
# 숫자로 풀기, 문자로 풀기
# 틀렸다는 이유는 모르겠다...!
# 브루트 포스일듯
#나눗셈에서는 항상 zerodivision 조심!!
# 다른 풀이는 그냥 곱한다 같긴한데
#내가 연산이 더 적어
######반례 12301 이 no가 되어야해 지금은 0이 나오면 양쪽다 0이 되버려
# 나눗셈으로 해버리면 0이 하나라도 있으면 c는 계속 0이 되네

a = []
[a.append(int(i)) for i in input()]

b=1
c=1
if len(a) == 1:
    print('NO')
elif a.count(0) > 1:
    print('YES')
elif a.count(0) == 1:
    print('NO')
else:
    for i in range(len(a)):
        if a[i] != 0:
            c *= a[i]
    d = 1
    for i in a:
        b *= i
        c //= i

        if b == c:
            print('YES')

            break
        # if b == d and c == 1:## 1221때문에 안돼. 물론 break 쓰면 되지만 끝까지 비교를 안하게 되서 안돼
        d += 1
        if d == len(a):  # 조건을 하느니 count를 셌어
            print('NO')
            break
        # elif i == a[len(a)-1]: # 인덱스가 아닌 value로 비교해서 안돼 반례:4729382 넣어보셍 2가 2개면서 마지막이라 두번뜰꺼임