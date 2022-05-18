#a = int(input())
import sys
a = int( sys.stdin.readline())

for i in range(1,a+1):
    x,y =map(int,input().split())
    print('Case #{0}: {1}'.format(i,x+y))
    #print("Case #%d: %d"%(i+1, A+B))



