# 다시 풀어봐
# format 문제가 될수도 rjust 문제가 될수도
# format 지정자
## < 왼쪽 > 오른쪽 ^ 가운데 정렬
## 공백을 -로 채우고 싶다면
# {:->4} 이런식이 되어야함
# {:>-4} 가 되면 오류 ValueError: Sign not allowed in string format specifier 뜸
# %-5 는 가능



a = int(input())
for i in range(1,a+1):
    print('{0:>{1}}'.format('*'*i,a))
    #print('{0:>{1}s}'.format('*'*i,a))
    '''
    # 매개변수 이용가능 
    print("{star:>{n}s}".format(star = ('*'*i),n = n))
    '''
'''#다른 사람 풀이
for i in range(1, a+1):
    print(' '*(a-i),'*'*i)

'''

'''#다른 사람 풀이
for i in range(1,a+1):
    star = '*'*i
    print(star.rjust(a))
'''