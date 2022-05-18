## 다시 해보셈
m,n = map(int, input().split())
li = [list(input()) for _ in range(m)]
count = 0
row_count = 0
col_count = 0

for i in li:
    if not i.count('X'):
        row_count += 1

for j in range(n):
    if not [li[i][j] for i in range(m)].count('X'):
        col_count += 1

print(max(row_count,col_count))



