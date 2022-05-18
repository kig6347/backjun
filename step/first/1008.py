##python에서는 double이 없고
## 묵시적 형변환이 존재함을 보여주는 문제
## round 함수 사용법

a,b = map(int,input().split())
print(a/b)


'''다른사람

a,b = input().split()
a = float(a)
b = float(b)
#print(a/b)
print(round(a/b,9))

'''