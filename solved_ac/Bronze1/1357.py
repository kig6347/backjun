#다시 해보셍
## 나도 잘 풀었는데 효율성 제로야. 다른사람이 훠우워어ㅜㄹ씬 우수해
#문법들은 맞았고 개념도 맞았어 근데 너무 불필요한게 많아
# str을 int를 이용해  앞의 00을 해결하는 문제
## join 사용법, [::-1] 행렬 거꾸로 바꾸는 법
## 1000 1 ==> 2 , 5 5 = 1



x,y = input().split()
x1 = list(x)
y1 = list(y)

x1 =x1[::-1]
# sort 하면 내림차순 오름차순으로 거꾸로가 아니야
y1 =y1[::-1]
x1= "".join(x1) #x1.join()이 아니고 문법이 "".join(x1)이야.
y1= "".join(y1)
x1=list(str(int(x1)))
y1=list(str(int(y1)))
x1= "".join(x1) #x1.join()이 아니고 문법이 "".join(x1)이야.
y1= "".join(y1)
c = int(x1)+int(y1)
d = list(str(c))
d = d[::-1]
d = "".join(d)
d=list(str(int(d)))
print("".join(d))

'''#다른 사람 풀이
x,y = map(str,input().split())
s = str( int(x[::-1])+int(y[::-1]))
print(int(s[::-1]))

'''