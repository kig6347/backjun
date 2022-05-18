# a를 굳이 사용하지 않아도 된다.
## 다른 아이디어로 sort를 해도 된다.
a = int(input())
#li = []
#[li.append(i) for i in input().split()]

b = list(map(int,input().split()))
print(min(b),max(b))
'''다른 사람 풀이
a = int(input())
array = list(map(int,input().split()))
array.sort()
print(array[0],array[-1]
# print(array[0],array[a-1]
'''

