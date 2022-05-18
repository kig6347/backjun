# a= list(input().split) 하고 a= [list(input().split)] 하고 다르다.
# 이유는 list는 함수로 형태를 바꾸는 거고 []는 배열 크기 지정한거니까
# list([1,2,3,4,5]) --> [1, 2, 3, 4, 5]
# [[1, 2, 3, 4, 5]] --> [[1, 2, 3, 4, 5]] 가 나온다.

a = int(input())
for i in range(a):
    sum = 0
    b = list(input().split('X'))
    for i in b:
        l = len(i)
        if l == 0:
            continue
        else:
            sum += (l* (l+1) )//2
    print(sum)
