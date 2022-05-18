# sum() 함수 알면 쉬워
# sum() 뒤에 list와 같은 순서 배열이 들어가면되는.
# 다른 사람 풀이의 방식을 처음 봤다.\
##print로 range(1,4) 를 출력하니 range(1,4) 가 나온다.
## list형태도 아니고 수 형태도 아닌데 어떻게 되는거지?
### https://stackoverflow.com/questions/43776128/what-is-the-return-value-of-the-range-function-in-python
## 참고 list(range(1,5))하면 볼수 있데
sum =0
for i in range(1,a+1):
    sum += i
print(sum)

'''다른 사람 풀이
print(sum(range(1,int(input())+1)))
'''