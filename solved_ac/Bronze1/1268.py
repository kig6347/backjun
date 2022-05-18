### 꼭 다시 해보렴
### 런타임에러 못고침
### 한글 지울것

cl = []
number = int(input())
answer = [[0]*5 for _ in range(number)]

cl.extend([list(map(int,input().split())) for _ in range(number)])

for gkrsus in range(5):
    for dlfma in range(number):
        for qksqhr in range(dlfma+1,number):
            #if dlfma == qksqhr:
            #    pass
            if cl[dlfma][gkrsus] == cl[qksqhr][gkrsus]:
                answer[qksqhr][dlfma] =1
                answer[dlfma][qksqhr] = 1 ### 학년별 가상의 표 생성, x = 이름 , y= 이름
print(answer)
cnt = []
for s in answer:
    cnt.append(s.count(1))
print(cnt.index(max(cnt))+1) # +1은 index 반환시 0부터 시작하기에.

