# 문자열 list로 안받고 배열 인덱스로 들어가도 됨
a = int(input())
b = input()
sum = 0
for i,j in enumerate(b[::-1]):
    q = int(j)*a
    print(q)
    q *= 10**int(i)
    sum += q

print(sum)
'''다른사람
A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈
'''
