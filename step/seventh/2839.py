a = int(input())
count = 9999
b = a//5

for i in range(b+1):
    if (a -(5*i)) %3 ==0:
        x = ((a -(5*i))//3)
        y = i
        count = min(count, x+ y)

print(-1 if count == 9999 else count )
