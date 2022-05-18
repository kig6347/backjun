a= input().split()
b = [int(a[i][::-1]) for i in range(2)]
print(max(b))
