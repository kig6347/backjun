# 나는 주로 0이면 false 아닌숫자 True 조건을 이용함
# 이게 헷갈리면 (year%4 == 0) 이렇게 지정 해도 댐
# not a % 4 and a % 100 여기서 앞에만 not이 적용됨
# not( a % 4 and a % 100) 이렇게 할경우 ()에서의 True, False가 결정나기에 사용x
# not a % 4 and not a % 100 하면 앞뒤로 not 적용
a = int(input())
if not a % 4 and a % 100:
    print(1)
elif not a % 400:
    print(1)
else: print(0)