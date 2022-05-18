#두번째 시도
sum = 0
for i in map(int,input().split()):
    sum += pow(i,2)
print(sum%10)

'''
#나의 첫번째 시도
a,b,c,d,e = map(int,input().split())
# pow() 내장함수 또는 ** 사용
print((pow(a,2) + pow(b,2) + pow(c,2) + pow(d,2) + pow(e,2)) % 10)
'''

