# print(sum(map(int,input()))) 이건 생각못함
# generater 에 대해 잘 알자.
import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()
sum = 0
for i in b:
    sum+=int(i)
print(sum)

'''#다른사람
n = input()
print(sum(map(int,input())))
'''