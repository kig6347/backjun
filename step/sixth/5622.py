alpha = [chr(i) for i in range(ord('A'),ord('Z')+1)]
read = input()
sum = 0
for i in read:
    sum += (alpha.index(i)//3) +3 if alpha.index(i) < 15 else 8 if 15 <= alpha.index(i) < 19 else 9 if 19 <= alpha.index(i) < 22 else 10
print(sum)