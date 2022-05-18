# 1 2 3 4 5 6 7
a = int(input())
count = 0
sum = 0
c = 0
d = 0

while True:
    count += 1
    sum += count
    if sum >= a:
        sum -= count
        break
a -= sum + 1

if count % 2:
    c = count - a
    d = a +1
else:
    c = a + 1
    d = count - a
print(c,d,sep='/')


