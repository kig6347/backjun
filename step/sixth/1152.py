## input().split()에 list() 를 안씌워도 list 형태로 나온다.
## .split()은 input().split()에서는 인자를 선택이 어렵고 따로 해야 seperater,batch가 먹힌다.
a = input().split()
print(len(a))