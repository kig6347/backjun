# 알파벳 배열 자동 생성
# aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
# aList =[chr(i) for i in range(97,123)]
# aList = list(map(chr, range(97, 123)))
#https://codetorial.net/python/strings.html
# 문자열 관련 함수  정리
#find()  검색후 인덱스를 반환, 못찾으면 -1 반환
#index() 인덱스 반환, find와 달리 못찾으면 에러
#rfind() 끝에서부터 처음으로 발견되는 문자
#rindex() 끝에서부터 처음으로 발견되는 문자열의 위치
#index()와 같이 rindex()는 문자열을 찾지 못할 경우 예외를 발생
#[print(chr(i)) for i in range(97,123)]

a = input()
for i in range(26):# 26 은 a~z 의 숫자
    print(a.find(chr(97+i)),end ='')

'''# 다른 사람
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
    
'''
'''다른 내 풀이 

import sys
input = sys.stdin.readline()
for i in list(map(chr,range(97,123))):
    if input.count(i) == 0:
        print(-1,end=' ')
        continue
    print(input.find(i),end = ' ')
print('')

'''
