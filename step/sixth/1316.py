
num = int(input())
count = 0
#a = input().split()
## 같은 list()가 나온다. split()의 align이 하나라서 다 들어가야 해서.
for _ in range(num):
    a = input()
    b = len(set(a))
    for i in range(1,len(a)):
        if a[i-1] == a[i]:
            #a = a.replace(a[i],'*',1)# 이렇게 하면 aadaa 에서 앞에서부터 하나를 바꾸기 때문에 원하는게 안바뀜, 애초에 이런 경우가 이러나면안댐
            a = a[:i-1]+a[i-1:].replace(a[i-1], '*', 1)

    a = a.replace('*','')

    if b == len(a):
        count += 1

print(count)
'''# 이방법 best 인듯
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
'''

'''#다른사람
# set개념을 직접 구함 .count로 다를때를 새로 만들어서
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)

'''