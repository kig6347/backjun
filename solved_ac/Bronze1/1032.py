a= int(input())
c= list(input())
for i in range(a-1):
    b = list(input())
    for j in range(len(c)):
        if c[j] is not b[j]:
            c[j] = "?"
print(''.join(c))

# 비교를 위해 list()로의 형변환이 반드시 필요했다.
# 또한 .join()을 모르니 풀수가 없었다.