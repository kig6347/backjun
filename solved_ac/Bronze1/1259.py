## 다시 해보셈

text = []
while True:
    a = input()

    if a == '0':
        break
    else:
        b = len(a)
        if b % 2:
            c = b // 2 + 1
        else:
            c = b // 2
        x = 0
        while x <= b//2:

            if a[x] == a[b-1-x]:
                count = 1
                x += 1
            else:
                count =0
                break

    if count:
        print('yes')
    else:
        print('no')


'''실패 
text = []
while True:
    a = input()

    if a == '0':
        break
    else:
        text.append(list(a))

for i in range(len(text)):
    b = len(text[i])
    if len(text[i]) % 2:
        c = b//2 + 1
    else:
        c = b//2
    if len(set(text[i])) <= c:
        print('yes')
    else:
        print('no')



# 나는 set 으로 풀고 싶엇는데 다들 거꾸로 배열을 생각했네
# 개념을 몰랐던... 나의 패배
# 반례가 있었네 1230231 이러면 set에서는 동일이라고 봄
'''

''''1번 예제

while True:
    flag = 1   # 숫자 하나만 들어갈 경우, yes로 처리하기 위해서 1로 초기화
    num = list(input())
    if num[0] == '0':
        break
    else:
        for i in range(len(num)//2):
            if num[i] == num[len(num)-1-i]:
                flag = 1
            else:
                flag = 0
                break  # 1223 같은 수를 위해서 반드시 필요
        if flag == 1:
            print("yes")
        else:
            print("no")
 


출처: https://gettingtoknowit.tistory.com/86 [흥미로운 IT]
'''


'''2번 예제
while True:
    n = input()
    
    if n =='0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
'''