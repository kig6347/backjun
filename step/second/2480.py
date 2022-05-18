## max() 함수를 알아서 접근할 수 있었다.
## list로 바꿔서 하려고도 생각했고 set도 하려고 했다.
##하지만 너무 많은 리소스를 사용할것으로 예상
#set의 경우 일일히 len과 count를 해야해서 패스
## list의 경우 list 인덱싱이 소비되기 때문문
a,b,c = map(int,input().split())
if a==b==c:
    count = 10000 + a*1000
elif a==b:
    count = 1000 + a*100
elif b == c:
    count = 1000 + b*100
elif a == c:
    count = 1000 + a*100
else:
    count = max(a,b,c) *100
print(count)