stri = input().upper()
compa = list(set(stri))
a= []
max = 0
cnf = ''
for i in compa:
    b = stri.count(i)
    if max == b:
        cnf = '?'
    elif b > max:
        max = b
        cnf = i
print(cnf)








