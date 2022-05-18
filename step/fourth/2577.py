## 곱셈값 반환 coprehension 찾아라
# set도 가능은 할듯

sum = 1
for _ in range(3):
    sum *= int(input())
# [sum *= int(input()) for _ in range(3)] ## 안돼네
answer = str(sum)
for i in range(10):
   print(answer.count(str(i)))

