#다시 풀어보셍
#컴파일 에러
# 정렬이 기억이 안났어. 다른 사람은 좀더 쉽게 풀었더라
# count를 이용했어. 나는 함수로 뭐가 빠른지느 모르겠네
# 추가로 compa를 2번 쓰는것 보다 문자열을 합치는것도 방법
l=0
o=0
v=0
e=0
answer = []
a = []
def compa(dusen,l,o,v,e):
    for i in dusen:
        if i is "L":
            l += 1
        elif i is "O":
            o += 1
        elif i is "V":
            v += 1
        elif i is "E":
            e += 1
    return l,o,v,e
dusen = input()
l,o,v,e = compa(dusen,l,o,v,e)
number = int(input())
for i in range(number):
    a.append(input())
    L,O,V,E = compa(a[i],l,o,v,e)
    answer.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
answer1 =[]
for q,j in enumerate(answer):
    if max(answer) == j:
        answer1.append(a[q])
answer1.sort()
print(answer1[0])

