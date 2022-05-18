# print() 의 option중에 sep과 end 가 있다.
# 문자를 표현하는 방법---파일포맷팅
# .format()
# f'{}' 변수 이름 그대로
# ""%()
## 괄호로 꼭 묶자

a,b = map(int,input().split())
'''
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
'''
print(a+b,a-b,a*b,a//b,a%b, sep='\n')
#print("%d\n%d\n%d\n%d\n%d"%(a+b, a-b, a*b, a/b, a%b)) 이것도 가능
