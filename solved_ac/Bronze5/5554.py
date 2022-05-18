
sum = 0
for i in range(4):
    sum += int(input())
#s = sum([int(input()) for _ in range(4)]) 이게 더 나은듯
print(sum//60)
print(sum%60)
