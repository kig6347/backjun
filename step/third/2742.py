## range 의 가감을 보여주는 예제
## range(6,0,-1) 이면 6부터 1까지 1씩 감소
## 두번째 인자의 경우
a = int(input())
[print(a - i) for i in range(a)]
#가능
#[print(i) for i in range(int(input()),0, -1)]
