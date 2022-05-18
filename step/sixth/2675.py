a = int(input())
for i in range(a):
    z, q = input().split()
    for j in q:
        print(j * int(z),end='')
    print('')
