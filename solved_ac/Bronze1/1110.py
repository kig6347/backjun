def A(B):
    a, b = B // 10, B % 10
    return (b*10)+((a+b)%10)
sum = int(input())
i = 0
num = sum
while True:
    i += 1
    num = A(num)
    if num == sum:
        break
print(i)



