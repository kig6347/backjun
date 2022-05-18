##반복이라는 점에서 // ,% 를 사용한다.
## 나처럼 마이너스를 주게 되면 검사할 사항이 많아지고 변수가 생긴다.
## 예를 들어 60이라고 하면 나머지는 0 으로 if >60 을 안할수 있게 된다.
## 아무때나 유용한건 아니고 이런 반복적인 결과가 나올떄 유리.

hour, min = map(int, input().split())
time = int(input())
min += time
while min > 59:
    min -= 60
    hour = hour + 1 if hour != 23 else 0
print(hour, min)

## while을 안쓸수 있네
'''다른사람
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)'''