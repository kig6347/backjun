# 소수점 몇자리를 나타내는 방법
# 1) round(40.00123, 3) ---> 40.001
# 2) ceil,floor
# 3) formating {:.3f}
# 3) 이떄 :.3은 전체 수가 3개고 :.3f는 소수점 수가 3개야.
# list indexing 잘 알자!! --> 아래 주석 avg = ~~~~
case = int(input())
for _ in range(case):
    count = 0
    li = list(map(int,input().split()))
    avg = (sum(li)/li[0] )-1
    #avg = sum(li[1:])/li[0]
    for i in li[1:]:
    #for i in li:
        #if i == li[0]: continue
        if i > avg:
            count += 1
    print('{:.3f}%'.format((count/li[0])*100))
    # round 도 방법이야


