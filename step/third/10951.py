# 10952와 달리 테스트 케이스의 종료조건이 없으므로
# 종료조건을 만들어주어야한다.
# 그래서 try except 구문이 된다.

while True:
    try:
        a,b = map(int,input().split())
    except:
        break
    print(a+b)
