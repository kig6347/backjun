## 문제를 이해 못해서 못풀고 다른 거 배껴옴 다시 풀어보셈

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for i in croatia:
    alpha = alpha.replace(i,'*')
print(len(alpha))


croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
