8장
문자바꾸기 (translate)
암호화
data = 'i love you'

table = str.maketrans('abcdefghijklmnopqrstuvwxyz','xyzabcdefghijklmnopqrstuvw')
data = data.translate(table)
print(data)
강도약해서 사용 거의 안함

복호화
data = 'f ilsb vlr'

table = str.maketrans('xyzabcdefghijklmnopqrstuvw','abcdefghijklmnopqrstuvwxyz')
data = data.translate(table)
print(data)



연습문제 10
리스트(시퀀스자료형)에서는 한 값 다음에 구분자 옴
문자열(시퀀스자료형)에서는 한 문자 다음에 구분자 옴

ss ='IT_CookBook'

# I#T#_#C------- 형태로 보여지게 만들어라

print("#".join(ss))



selfstudy 8-1
짝수글자는 그대로 표시 홀수번에는 #표시

ss='파이썬은완전재미있어요'

sslen = len(ss)
for i in range(0,sslen):
if i % 2 == 1:
print('#',end='')
else:
print(ss[i],end='')

code8-2 교재말고 다른 방법 사용해서 작성

inStr = ''

inStr = input('문자열을 입력하세요 : ')

str_len = len(inStr)

for i in range(0,str_len):
print(inStr[str_len-(i+1)],end='')

교수님 코드1

inStr = ''

inStr = input('문자열을 입력하세요 : ')

str_len = len(inStr)

for i in reversed(range(0,str_len)):
print(inStr[i],end='')

교수님 코드2

inStr = ''

inStr = input('문자열을 입력하세요 : ')

str_len = len(inStr)

for i in reversed(inStr):
print(i,end='')