# range(9) 하고 +1하는 것 보다
# range(1,10)이 효율적
a = int(input())
for i in range(9):
    print('{} * {} = {}'.format(a,i+1,a*(i+1)))

