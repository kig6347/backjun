#https://ywtechit.tistory.com/121 참고하삼
# 10보다 수가 작으면 앞에 0을 붙이기 무시해도 그만
## 어차피 뒤수에 영향 x
#문자열로 푸는 방법과 수로 푸는 방법 존재
#새로운 수 new_n을 구할 때 10으로 나누는 방법과 문자열인덱싱으로 제일 마지막의 값만 떼 오는 방법을 사용했는데, 메모리는 28776KB로 동일했고 실행시간이 64m/s, 72m/s로 10으로 나누는 방법이 8m/s로 근소하게 빨랐다
# break 시에 count의 위치 역시 중요
## 다른 사람의 경우 한번 실행되고 count 한다면 나는 미리 count 하고 검사함

a= int(input())
count = 1
b = a
while True:

    y = b%10
    b = (y + (b//10))%10 + y *10
    if a == b:
        print(count)
        break
    else:
        count += 1


'''다른사람
n = int(input())
check = n
flag = True
cnt = 0
 
# 10으로 나누는 방법
while flag:
    temp = int(n) // 10 + int(n) % 10
    new_n = str(n % 10) + str(temp % 10)
    cnt += 1
    if int(new_n) == check:
        flag = False
    n = int(new_n)
print(cnt)
 
# 문자열 인덱싱 이용한 방법
while flag:
    temp = int(n) // 10 + int(n) % 10
    new_n = str(n)[-1] + str(temp)[-1]
    cnt += 1
    if int(new_n) == check:
        flag = False
    n = new_n
print(cnt)

'''
