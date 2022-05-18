a = input()
a = a.lower()
b = set(a)
li = []
for i in b:
    li.append(a.count(i))
if li.count(max(li)) >1:
    print('?')