# 두문장이 같아. 하나는 append를 쓰고 하나는 그냥 list 뭐가 더 편할까? 후자가 가벼워보이네^^
# li = [int(input())%42 for _ in range(10)] 꼭 기억해
# 방법은 2가지 if x in arry,   set 이용방법

li = []
#[li.append(int(input())%42) for _ in range(10)]
li = [int(input())%42 for _ in range(10)]
answer = set(li)
print(len(answer))

