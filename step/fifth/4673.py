## 정답 못맞춤
#부르트 포스가 맞아
#문자 개수가 다를때 더하는 방법에 대한 고민이 부족했어 -> 물론 if로 나타낼수 있지만 그거보다 효율적인?
#for i in str(i) 로 푸네
# set() 함수 선언과 사용법
## add(), update(), remove()
# 다른 사람의 풀이에서 for num in numbers: 에서 num을 그대로 사용해 메모리를 줄인게 획기적이야
# 또한 문자열을 다룰땐 나누기로 다뤄도 되지만 str그대로 다루는것도 방법
## 여기선 2자리인지 3자리인지 모르니 str로 사용하는게 좋아
# 방법은 list에 전부 저장후 지워서 출력
# set이용해서 비교해서 없으면 출력

########### set 정렬방법
#1)sorted(s, key=float) --> 소수점 위에도고려
#sorted(s) --> 소수점 아래만 고려
#3) list로 반환후 정렬
#sorted()함수는 정렬 된 시퀀스 (list, tuple, string) 또는 정렬 된 컬렉션 (sets, dictionary)을 목록 형식으로 반환하는 Python의 내장 함수
## 대신 반환값이 없어 함수로 받아야함
# 2)sort()
#https://www.delftstack.com/ko/howto/python/sort-sets-python/
#https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=wideeyed&logNo=221745416992&redirect=Dlog&widgetTypeCall=true&directAccess=false
## sort는 원본 list 변환 sorted 는 반환값 존재


'''#다른사람
출처: https://hei-jayden.tistory.com/196?category=528821'''
'''#다른사람
#list에서 사용할 수 있는 함수를 활용한 코드
numbers = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10_000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)
'''

'''#다른사람
# set에서 사용할 수 있는 함수를 활용한 코드
numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)
'''

# li = list(range(1,10001)) 의 표현식도 알자!!
answer = set(range(1,10001))
li = set()
for i in range(1,10000):# 10000도 해야하는데 해봤자 list에 들어갈 필요가 없어서 제외 했어
    for j in str(i):
        i += int(j)
    li.add(i)
an = answer - li
for k in sorted(an): # sort(an) 은 런타임 에러가 난다.
    print(k)



