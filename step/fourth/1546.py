# python 평균 구하는 4가지 방법
# 1) for로 모두 더하고 개수 나누기
# 2) sum() 이용후 개수 나누기
# 3) numpy 이용 np.mean()
# 4) statiscics 라이브러리 이용
## 3.4 버전부터 가능하고 statiscics.mean() 내장함수 로 import statistics 해주면 됨

import sys
## 1~1000까지 라고 해서 sys 를 사용
# a= input()
a = int(sys.stdin.readline())
a_conver = list(map(int,sys.stdin.readline().split()))
max_value = max(a_conver)
answer = [(a_conver[i]/max_value)*100 for i in range(a)]
#print(answer)
print('{0}'.format(sum(answer) / a))

