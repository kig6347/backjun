# append 대신 []와 comprehension으로 받을수 있음을 기억
# 기억해 li = [int(input()) for _ in range(9)]

li = []
for i in range(9):
    li.append(int(input()))
#li = [int(input()) for _ in range(9)]
print(max(li),li.index(max(li))+1,sep='\n')